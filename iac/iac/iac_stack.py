import os
from aws_cdk import (
    aws_lambda as lambda_,
    Stack,
    aws_cognito,
    Duration,
    aws_iam
)
from constructs import Construct
from .dynamo_stack import DynamoStack
from .lambda_stack import LambdaStack
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.user_pool_arn = os.environ.get("USER_POOL_ARN")
        self.user_pool_id = os.environ.get("USER_POOL_ID")
        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")
        self.aws_region = os.environ.get("AWS_REGION")
        self.app_client_id = os.environ.get("APP_CLIENT_ID")

        self.dynamo_stack = DynamoStack(self)

        self.cognito_auth = CognitoUserPoolsAuthorizer(self, f"gaia_profile_cognito_cognito_auth_{self.github_ref_name}",
                                                       cognito_user_pools=[aws_cognito.UserPool.from_user_pool_arn(
                                                           self, f"gaia_profile_cognito_auth_userpool_{self.github_ref_name}",
                                                           self.user_pool_arn
                                                       )]
                                                       )
 
        self.rest_api = RestApi(self, f"GaiaProfile_RestApi_{self.github_ref_name}",
                                rest_api_name=f"GaiaProfile_RestApi_{self.github_ref_name}",
                                description="This is the GaiaProfile RestApi",
                                default_cors_preflight_options={
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                },
                                )

        ENVIRONMENT_VARIABLES = {
            "STAGE": self.github_ref_name.upper(),
            "USER_POOL_ID": self.user_pool_id,
            "USER_POOL_ARN":  self.user_pool_arn,
            "APP_CLIENT_ID": self.app_client_id,
            "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            "DYNAMO_PARTITION_KEY": "PK",
            "DYNAMO_SORT_KEY": "SK",
        }

        api_gateway_resource = self.rest_api.root.add_resource("mss-gaia-profile", default_cors_preflight_options={
            "allow_origins": Cors.ALL_ORIGINS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": Cors.DEFAULT_HEADERS
        }
        )

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=self.cognito_auth)
        
        for f in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table.grant_read_write_data(f)
        
        cognito_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "cognito-idp:*",
            ],
            resources=[
                self.user_pool_arn
            ]
        )

        for f in self.lambda_stack.functions_that_need_cognito_permissions:
            f.add_to_role_policy(cognito_admin_policy)
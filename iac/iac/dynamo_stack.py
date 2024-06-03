import os


from aws_cdk import (
    CfnOutput,
    aws_dynamodb,
    RemovalPolicy
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration

class DynamoStack(Construct):

        def __init__(self, scope: Construct) -> None:
            super().__init__(scope, "GaiaProfile_Dynamo")

            self.github_ref_name = os.environ.get("GITHUB_REF_NAME")

            REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.github_ref_name else RemovalPolicy.DESTROY

            self.dynamo_table = aws_dynamodb.Table(
                self, "Gaia_Profile_Table",
                partition_key=aws_dynamodb.Attribute(
                    name="PK",
                    type=aws_dynamodb.AttributeType.STRING
                ),
                point_in_time_recovery=True,
                billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
                removal_policy=REMOVAL_POLICY,
                stream=aws_dynamodb.StreamViewType.NEW_IMAGE
            )
            
            CfnOutput(self, 'DynamoProfileRemovalPolicy',
                        value=REMOVAL_POLICY.value,
                        export_name=f'GaiaProfile{self.github_ref_name}DynamoRemovalPolicyValue')
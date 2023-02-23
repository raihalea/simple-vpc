from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class SimpleVpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        vpc = ec2.Vpc(
            self,
            "vpc",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    name="private", subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                ),
            ],
        )

        vpc.add_interface_endpoint("ssm_endpoint",
            service=ec2.InterfaceVpcEndpointAwsService.SSM
        )

        vpc.add_interface_endpoint("ec2messages_endpoint",
            service=ec2.InterfaceVpcEndpointAwsService.EC2_MESSAGES
        )

        vpc.add_interface_endpoint("ssmmessages_endpoint",
            service=ec2.InterfaceVpcEndpointAwsService.SSM_MESSAGES
        )
        
        vpc.add_gateway_endpoint("s3_endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3
        )

# Simple VPC
AWS CDK(Python)で作る単純なVPCです。
以下のリソースが作成されます。

- VPC
- Public Subnet x2
- Private Subnet x2
- IGW
- NAT GW
- VPC Endpoint(ssm/ec2messages/ssmmessages/S3)

SSMでの接続ができるようにSSM用のVPCエンドポイントとS3のゲートウェイエンドポイントを作成します。

from botocore.exceptions import NoCredentialsError

from aws_svce import AwsSvce
class RdsService:
    def __init__(self, aws_service:AwsSvce):
        self.rds_client = aws_service.rds_client

    def generate_db_auth_token(self,DB_HOST,DB_PORT,DB_USER,REGION):
        return self.rds_client.generate_db_auth_token(
            DBHostname=DB_HOST,
            Port=DB_PORT,
            DBUsername=DB_USER,
            Region=REGION
        )
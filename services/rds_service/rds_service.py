from botocore.exceptions import NoCredentialsError

from aws_svce import AwsSvce
class RdsService:
    def __init__(self, aws_service:AwsSvce):
        self.__rds_client = aws_service.rds_client

    def generate_db_auth_token(self,DB_HOST,DB_PORT,DB_USER,REGION):
        try:
            return True, self.__rds_client.generate_db_auth_token(
                DBHostname=DB_HOST,
                Port=DB_PORT,
                DBUsername=DB_USER,
                Region=REGION
            )
        except NoCredentialsError:
            return False, "Credentials not available"
        except Exception as ex:
            return False , str(ex)
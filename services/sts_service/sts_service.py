from botocore.exceptions import NoCredentialsError

from aws_svce import AwsSvce
class StsService:
    def __init__(self, aws_service:AwsSvce):
        self.__sts_client = aws_service.sts_client

    def assume_role(self,role_arn,role_session_name,duration_seconds,region):
        try:
            response = self.__sts_client.assume_role(
                RoleArn=role_arn,
                RoleSessionName=role_session_name,
                DurationSeconds=duration_seconds
                )
            return True,AwsSvce(region=region,
                access_key=response['Credentials']['AccessKeyId'],
                secret_key=response['Credentials']['SecretAccessKey'],
                session_token=response['Credentials']['SessionToken'])
        except NoCredentialsError:
            return False, "Credentials not available"
        except Exception as ex:
            return False , str(ex)
        
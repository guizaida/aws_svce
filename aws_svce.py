import boto3


class AwsSvce(object):
    '''
    Example of use \n

    from dx_project import AwsSvce\n
    AwsSvce(\n
    region='',\n
    access_key='',\n
    secret_key=''\n
    )
    '''
    __slots__ = ('__region', '__access_key', '__secret_key', '__s3_client', '__sys_client',
                 '__lambda_client', '__cloudwatch_logs_client', '__endpoint_url', '__rds_client', '__sts_client', '__step_function_client', '__secret_manager_client', '__session_token')

    def __init__(self, region: str = None, access_key: str = None, session_token: str = None, secret_key: str = None, endpoint_url: str = None):
        self.__region = region
        self.__access_key = access_key if access_key != '' else None
        self.__secret_key = secret_key if secret_key != '' else None
        self.__endpoint_url = endpoint_url if endpoint_url != '' else None
        self.__session_token = session_token if session_token != '' else None
        self.__s3_client = self.__create_aws_client('s3')
        self.__sys_client = self.__create_aws_client('ssm')
        self.__lambda_client = self.__create_aws_client('lambda')
        self.__cloudwatch_logs_client = self.__create_aws_client('logs')
        self.__rds_client = self.__create_aws_client('rds')
        self.__sts_client = self.__create_aws_client('sts')
        self.__step_function_client = self.__create_aws_client('stepfunctions')
        self.__secret_manager_client = self.__create_aws_client('secretsmanager')

    def __create_aws_client(self, svce_name: str):
        if self.__access_key and self.__secret_key:
            if self.__session_token:
                return boto3.client(
                    service_name=svce_name,
                    aws_access_key_id=self.__access_key,
                    aws_secret_access_key=self.__secret_key,
                    region_name=self.__region,
                    aws_session_token=self.__session_token
                )
            else:
                return boto3.client(
                    service_name=svce_name,
                    aws_access_key_id=self.__access_key,
                    aws_secret_access_key=self.__secret_key,
                    region_name=self.__region
                )
        elif self.__endpoint_url:
            return boto3.client(
                service_name=svce_name,
                endpoint_url=self.__endpoint_url
            )
        else:
            return boto3.client(svce_name, region_name=self.__region)

    @property
    def s3_client(self):
        return self.__s3_client

    @property
    def sys_manger_client(self):
        return self.__sys_client

    @property
    def lambda_client(self):
        return self.__lambda_client

    @property
    def cloudwatch_logs_client(self):
        return self.__cloudwatch_logs_client

    @property
    def rds_client(self):
        return self.__rds_client

    @property
    def sts_client(self):
        return self.__sts_client

    @property
    def step_function_client(self):
        return self.__step_function_client

    @property
    def step_function_client(self):
        return self.__step_function_client

    @property
    def secret_manager_client(self):
        return self.__secret_manager_client

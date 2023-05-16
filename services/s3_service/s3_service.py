from botocore.exceptions import NoCredentialsError
class S3Service:
    def __init__(self, aws_service):
        self.s3_client = aws_service.s3_client

    def upload_file(self, bucket_name, file_name, object_name=None):
        object_name = object_name if object_name is not None else file_name
        try:
            self.s3_client.upload_file(file_name, bucket_name, object_name)
        except NoCredentialsError:
            return False, "Credentials not available"
        return True, 'File uploaded successfully'

    def generate_presigned_url(self, bucket_name, object_name, expiration=3600):
        try:
            response = self.s3_client.generate_presigned_url('get_object',
                                                            Params={'Bucket': bucket_name,
                                                                    'Key': object_name},
                                                            ExpiresIn=expiration)
        except Exception as e:
            return False, str(e)
        return True, response

    def get_object(self, bucket_name, object_name):
        try:
            response = self.s3_client.get_object(Bucket=bucket_name, Key=object_name)
        except Exception as e:
            return False, str(e)
        return True, response['Body'].read()

    def upload_file_and_generate_url(self, bucket_name, file_name, object_name=None, expiration=3600):
        success, message = self.upload_file(bucket_name, file_name, object_name)
        if not success:
            return False, message
        
        object_name = object_name if object_name is not None else file_name
        success, url = self.generate_presigned_url(bucket_name, object_name, expiration)
        if not success:
            return False, url

        return True, url

    def list_buckets(self):
        try:
            response = self.s3_client.list_buckets()
        except Exception as e:
            return False, str(e)
        return True, [bucket['Name'] for bucket in response['Buckets']]

    def list_objects_v2(self, bucket_name, prefix=None):
        try:
            if prefix:
                response = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
            else:
                response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        except Exception as e:
            return False, str(e)
        return True, response.get('Contents', [])

    def upload_file_with_put(self, bucket_name, file_content, object_name):
        """
        使用 put_object 方法上傳檔案內容到 S3。
        :param bucket_name: S3 桶子名稱
        :param file_content: 要上傳的檔案的內容，應該是一個 bytes-like 物件
        :param object_name: 在 S3 中的物件名稱
        :return: 上傳成功返回 True 和 S3 物件的鍵，失敗返回 False 和錯誤訊息
        """
        try:
            self.s3_client.put_object(Bucket=bucket_name, Key=object_name, Body=file_content)
            return True, object_name
        except Exception as e:
            return False, str(e)
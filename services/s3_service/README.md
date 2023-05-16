# S3Service 使用說明

`S3Service` 是一個用於操作 AWS S3 服務的 Python 類別。它提供了一些常用的 S3 功能，包括上傳檔案、生成預簽名 URL、獲取 S3 物件內容，以及列出所有的 S3  Bucket 和 Bucket 中的物件。

## 安裝

首先，確保你已經安裝了 `boto3`：

```shell
pip install boto3
```

## 使用方式

首先，你需要建立一個 AwsSvce 的實例：
```python
from your_module import AwsSvce
aws_svce = AwsSvce(region='your-region', access_key='your-access-key', secret_key='your-secret-key')
```

接著，使用 AwsSvce 的實例來創建 S3Service 現在你可以使用 S3Service 提供的方法了。以下是一些範例：

## 上傳檔案：

```python
from aws_services.s3_service import S3Service

s3_service = S3Service(region='your-region', access_key='your-access-key', secret_key='your-secret-key')
success, message = s3_service.upload_file('your-bucket-name', 'your-file-name')
if success:
    print("File uploaded successfully")
else:
    print("Failed to upload file: ", message)

```
## 生成預簽名 URL：

```python
from aws_services.s3_service import S3Service

s3_service = S3Service(region='your-region', access_key='your-access-key', secret_key='your-secret-key')
success, url_or_message = s3_service.generate_presigned_url('your-bucket-name', 'your-object-name')
if success:
    print("URL: ", url_or_message)
else:
    print("Failed to generate URL: ", url_or_message)
```
## 獲取物件：

```python
from aws_services.s3_service import S3Service

s3_service = S3Service(region='your-region', access_key='your-access-key', secret_key='your-secret-key')
success, content_or_message = s3_service.get_object('your-bucket-name', 'your-object-name')
if success:
    print("Content: ", content_or_message)
else:
    print("Failed to get object: ", content_or_message)
```
## 上傳檔案並生成預簽名 URL：

```python
success, url_or_message = s3_service.upload_file_and_generate_url('your-bucket-name', 'your-file-name')
if success:
    print("URL: ", url_or_message)
else:
    print("Failed: ", url_or_message)

```
## 列出所有S3bucket:

```python
from aws_services.s3_service import S3Service

s3_service = S3Service(region='your-region', access_key='your-access-key', secret_key='your-secret-key')
success, buckets_or_message = s3_service.list_buckets()
if success:
    print("Buckets: ", buckets_or_message)
else:
    print("Failed: ", buckets_or_message)
```

## 列出 Bucket 中的所有物件：

```python
from aws_services.s3_service import S3Service

s3_service = S3Service(region='your-region', access_key='your-access-key', secret_key='your-secret-key')
success, objects_or_message = s3_service.list_objects_v2('your-bucket-name')
if success:
    for obj in objects_or_message:
        print(obj['Key'])
else:
    print("Failed: ", objects_or_message)
```

## 使用 put_object 上傳檔案內容

這個功能讓你能夠直接將檔案的內容上傳到 S3，而不需要先將檔案存儲到本地。這是一個非常有用的功能，特別是當你處理的檔案內容是在記憶體中產生的，並且你希望避免寫入磁碟的額外開銷時。

要使用這個功能，你需要創建一個 `S3Service` 物件，然後調用其 `upload_file_with_put` 方法。這個方法需要三個參數：`bucket_name` 是你想要上傳到的 S3 桶子的名稱，`file_content` 是你想要上傳的檔案的內容（應該是一個 bytes-like 物件），`object_name` 是在 S3 中的物件名稱。

下面是一個例子：

```python
from aws_services.s3_service import S3Service

s3_service = S3Service(region='your-region', access_key='your-access-key', secret_key='your-secret-key')

file_content = b"This is the content of the file."
bucket_name = "your-bucket-name"
object_name = "your-object-name"

result, message = s3_service.upload_file_with_put(bucket_name, file_content, object_name)
if result:
    print(f"Uploaded file successfully. S3 object key: {message}")
else:
    print(f"Failed to upload file. Error: {message}")

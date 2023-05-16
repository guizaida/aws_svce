## 使用指南

這是一個用於操作 AWS 服務的範例程式庫。以下是如何使用它的步驟：

## 安裝

在開始之前，請確保已經安裝了 boto3 庫。你可以使用以下指令進行安裝：

```shell
pip install boto3
```
## 使用範例

以下是使用 AwsSvce 類別的範例程式碼：
```python
from dx_project import AwsSvce

# 創建 AwsSvce 實例
svce = AwsSvce(
    region='<區域>',
    access_key='<訪問金鑰>',
    secret_key='<密鑰>',
    session_token='<會話令牌>',
    endpoint_url='<終端點 URL>'
)

# 使用 S3 服務客戶端
s3_client = svce.s3_client

# 使用系統管理服務客戶端
sys_manager_client = svce.sys_manager_client

# 使用 Lambda 服務客戶端
lambda_client = svce.lambda_client

# 使用 CloudWatch Logs 服務客戶端
cloudwatch_logs_client = svce.cloudwatch_logs_client

# 使用 RDS 服務客戶端
rds_client = svce.rds_client

# 使用 STS 服務客戶端
sts_client = svce.sts_client

# 使用 Step Functions 服務客戶端
step_function_client = svce.step_function_client

# 使用 Secrets Manager 服務客戶端
secret_manager_client = svce.secret_manager_client

# 現在，你可以使用這些客戶端對相應的 AWS 服務進行操作了

```

## 注意事項
- 如果提供了訪問金鑰和密鑰，將使用這些值來驗證客戶端。
- 如果提供了終端點 URL，將使用該 URL 作為服務的端點。
- 如果未提供訪問金鑰、密鑰和終端點 URL，將使用預設配置進行驗證和連接。
- 希望這個使用指南對你有所幫助！如果你有任何疑問或問題，請隨時向我提問。
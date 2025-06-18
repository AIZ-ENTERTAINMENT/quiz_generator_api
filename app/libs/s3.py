import os

import boto3
from fastapi import HTTPException

from app.libs.logger_config import logger


class S3Client:
    def __init__(self):
        access_key = os.environ["AWS_ACCESS_KEY"]
        secret_key = os.environ["AWS_SECRET_KEY"]
        self.client = boto3.client(
            "s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key
        )

    def upload(self, file, key, bucket="quiz-generator-bucket") -> str:
        try:
            self.client.upload_fileobj(
                file, bucket, key, ExtraArgs={"ContentDisposition": "inline"}
            )
        except Exception as e:
            logger.error(
                f"{__name__} - Error - "
                + f"Failed to upload file to S3. file: {file}, bucket: {bucket}, key: {key}",
                exc_info=e,
            )
            raise HTTPException(
                400, detail={"error": "이미지 업로드에 실패했습니다.", "code": "400"}
            )
        return f"https://{bucket}.s3.ap-northeast-2.amazonaws.com/{key}"

    def download(self, file_path, key, bucket="quiz-generator-bucket"):
        self.client.download_file(bucket, key, file_path)

    def delete(self, key, bucket="quiz-generator-bucket"):
        self.client.delete_object(Bucket=bucket, Key=key)

    def auto_key_select_delete(self, key, bucket="quiz-generator-bucket"):
        key = key.split("ap-northeast-2.amazonaws.com/")[-1]
        self.client.delete_object(Bucket=bucket, Key=key)

    def copy(
        self,
        source_key,
        dest_key,
        source_bucket="quiz-generator-bucket",
        dest_bucket="quiz-generator-bucket",
    ):
        source_key = source_key.split("ap-northeast-2.amazonaws.com/")[-1]
        self.client.copy_object(
            CopySource={"Bucket": source_bucket, "Key": source_key},
            Bucket=dest_bucket,
            Key=dest_key,
        )
        return f"https://{dest_bucket}.s3.ap-northeast-2.amazonaws.com/{dest_key}"


if __name__ == "__main__":
    s3 = S3Client()
    s3.upload("aiz-ailab", "quiz-generator-bucket", "quiz_profile/test.png")

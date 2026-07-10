import boto3
import logging
import time
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Create S3 client
s3 = boto3.client("s3")


class S3Client:

    def upload_file(self, file_name, bucket, object_name):
        retries = 3

        for attempt in range(retries):
            try:
                s3.upload_file(file_name, bucket, object_name)

                logger.info(
                    f"Uploaded {file_name} to {bucket}/{object_name}"
                )

                return True

            except ClientError as e:

                logger.warning(
                    f"Retry {attempt + 1} failed..."
                )

                if attempt < retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    logger.error(e)
                    raise

    def list_objects(self, bucket):
        try:
            response = s3.list_objects_v2(Bucket=bucket)

            if "Contents" in response:
                for obj in response["Contents"]:
                    logger.info(obj["Key"])

            return response

        except ClientError as e:
            logger.error(e)
            raise

    def download_file(self, bucket, object_name, file_name):
        retries = 3

        for attempt in range(retries):
            try:
                s3.download_file(bucket, object_name, file_name)

                logger.info(
                    f"Downloaded {object_name}"
                )

                return True

            except ClientError as e:

                logger.warning(
                    f"Retry {attempt + 1} failed..."
                )

                if attempt < retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    logger.error(e)
                    raise

    def generate_presigned_url(self, bucket, object_name, expiration=3600):
        try:
            url = s3.generate_presigned_url(
                "get_object",
                Params={
                    "Bucket": bucket,
                    "Key": object_name
                },
                ExpiresIn=expiration
            )

            logger.info("Pre-signed URL generated successfully")

            return url

        except ClientError as e:
            logger.error(e)
            raise
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class MyCustomLibrary:
    def __init__(self):
        print("Initialized Library!")

    def my_keyword(self, text):
        """Logs the provided text."""
        print(f"My Keyword executed with: {text}")

    def verify_aws_connection1(self):
        """
        Verifies AWS connection by listing S3 buckets.
        Raises an exception if connection fails.
        """
        try:
            s3 = boto3.client('s3')
            s3.list_buckets()
        except NoCredentialsError:
            raise AssertionError("AWS credentials not found.")
        except ClientError as e:
            raise AssertionError(f"Failed to connect to AWS: {e}")
        except Exception as e:
            raise AssertionError(f"Unexpected error: {e}")

    def Verify_AWS_Connection(self):
        """Robot Framework keyword for verifying AWS connection."""
        self.verify_aws_connection1()

    def validate_s3_bucket1(self, bucket_name):
        """
        Validates if the specified S3 bucket exists and is accessible.
        Raises an exception if the bucket does not exist or is not accessible.
        """
        try:
            s3 = boto3.client('s3')
            s3.head_bucket(Bucket=bucket_name)
        except NoCredentialsError:
            raise AssertionError("AWS credentials not found.")
        except ClientError as e:
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                raise AssertionError(f"Bucket '{bucket_name}' does not exist.")
            else:
                raise AssertionError(f"Failed to access bucket '{bucket_name}': {e}")
        except Exception as e:
            raise AssertionError(f"Unexpected error: {e}")

    def Validate_S3_Bucket(self, bucket_name):
        """Robot Framework keyword for validating S3 bucket existence and access."""
        self.validate_s3_bucket1(bucket_name)

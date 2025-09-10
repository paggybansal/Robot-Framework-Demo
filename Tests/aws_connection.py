import logging

import pytest

from BucketWrapper import BucketWrapper
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
s3_client = boto3.resource("s3")

bucket_wrapper = BucketWrapper(s3_client.Bucket('123-test-my-first-bucket-1234'))
#bucket_wrapper.create()
bucket_wrapper.delete()


@pytest.mark.parametrize('error', [None, 'TestException'])
def test_list(make_stubber, error_code):
    s3_resource = boto3.resource("s3")
    s3_stubber = make_stubber(s3_resource.meta.client)
    bucket_name = "test-bucket_name"
    wrapper = BucketWrapper(s3_resource.Bucket(bucket_name))
    created_buckets = [
        s3_resource.Bucket(f"{bucket_name}-{ind}") for ind in range(0, 5)
    ]

    s3_stubber.stub_list_buckets(created_buckets, error_code=error_code)

    if error_code is None:
        got_buckets = wrapper.list(s3_resource)
        assert got_buckets == created_buckets
    else:
        with pytest.raises(ClientError) as exc_info:
            wrapper.list(s3_resource)
        assert exc_info.value.response["Error"]["Code"] == error_code

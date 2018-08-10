import io

import boto3
import moto
import pytest


@pytest.mark.parametrize('region_name', [
    'us-east-1',
    'us-west-1',
    'us-west-2',
    'eu-west-1',
    'eu-cental-1',
    'ap-northeast-1',
    'ap-northeast-2',
    'ap-southeast-1',
    'ap-southeast-2',
    'sa-east-1',
])
@moto.mock_s3
def test_mock_s3(region_name):
    s3session = boto3.Session(region_name=region_name)
    s3res = s3session.resource('s3')
    s3bucket = s3res.Bucket('test_bucket')
    s3bucket.create()
    s3obj = s3res.Object('test_bucket', 'test_object.txt')
    s3obj.put(Body=io.BytesIO(b'abc'))
    data = s3obj.get()['Body'].read()
    assert b'abc' == data

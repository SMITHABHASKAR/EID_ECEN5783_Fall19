import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAIOK6T75MCFEYUTMA'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was uploaded")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('loom2', 'qrcoderecogn', 'loom2')
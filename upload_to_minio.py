from minio import Minio
from minio.error import S3Error
import os
from settings import CONFIG_DIR
import yaml

# Load Config From settings.yaml
def load_config():
    settings_file = os.path.join(CONFIG_DIR, 'settings.py')
    with open(settings_file, 'r') as f:
        return yaml.safe_load(f)

def upload_file_to_minio(file_path, object_name):
    config = load_config()
    minio_config = config['minio']

    # Create Minio client
    client = Minio(
        minio_config['endpoint'].replace("http://", ""),
        access_key=minio_config['access_key'],
        secret_key=minio_config['secret_key'],
        secure=False
    )

    # Upload to Bucketlist
    try:
        client.fget_object(
            bucket_name=minio_config['bucket_name'],
            object_name=object_name,
            file_path=file_path
        )
        print(f"Uploaded {file_path} as {object_name} into bucket '{minio_config['bucket_name']}'")

    except S3Error as e:
        print('Upload Failed')
        print(f'Error: {e}')

if __name__ == '__main__':
    local_file = './data/processed/flight_prices_cleaned.parquet'
    minio_object_name = 'flight_prices/flight_prices_cleaned.parquet'
    upload_file_to_minio(local_file, minio_object_name)

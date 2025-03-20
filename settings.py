import os

# Root
base_dir = os.getcwd() + os.sep
print(f'Directory Paht is {base_dir}')

# Datalake Local
DATA_DIR = os.path.join(base_dir, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Docker compose directory
DOCKER_DIR = os.path.join(base_dir, 'docker')

# Config
CONFIG_DIR = os.path.join(base_dir, 'config')
SETTING_YAML = os.path.join(CONFIG_DIR, 'settings.yaml')

# MinIO Config (For Connect API)
MINIO_CONFIG = {
    'endpoint': 'http://localhost:9000',
    'access_key': 'admin',
    'secret_key': 'admin123',
    'bucket': 'flight-data'
}
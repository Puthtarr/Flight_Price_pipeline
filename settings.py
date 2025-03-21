import os

# Root Directory
base_dir = os.getcwd() + os.sep
print(f'Directory Path is {base_dir}')

# Datalake Local Directories
DATA_DIR = os.path.join(base_dir, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Docker Directories
DOCKER_DIR = os.path.join(base_dir, 'docker')
DOCKER_MINIO_DIR = os.path.join(DOCKER_DIR, 'minio-datalake')
DOCKER_PRESTO_DIR = os.path.join(DOCKER_DIR, 'presto')
DOCKER_PRESTO_CATALOG_DIR = os.path.join(DOCKER_PRESTO_DIR, 'catalog')

# Config Directory
CONFIG_DIR = os.path.join(base_dir, 'config')
SETTING_YAML = os.path.join(CONFIG_DIR, 'settings.yaml')

# MinIO Config (Connect API / SDK)
MINIO_CONFIG = {
    'endpoint': 'http://localhost:9000',
    'access_key': 'admin',
    'secret_key': 'admin123',
    'bucket': 'flight-data'
}

# Presto Config
PRESTO_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'catalog': 'hive',
    'schema': 'default'
}

# ฟังก์ชันสำหรับสร้าง Directory พร้อมเช็คซ้ำ
def create_directories():
    directories = [
        DATA_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        CONFIG_DIR,
        DOCKER_DIR,
        DOCKER_MINIO_DIR,
        DOCKER_PRESTO_DIR,
        DOCKER_PRESTO_CATALOG_DIR
    ]

    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f'Created directory: {directory}')
        else:
            print(f'Already Exist: {directory}')


if __name__ == "__main__":
    create_directories()

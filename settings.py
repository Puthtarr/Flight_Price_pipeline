import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

AVIATIONSTACK_ACCESS_KEY = os.getenv("AVIATIONSTACK_ACCESS_KEY")
EXCHANGE_RATE_ACCESS_KEY = os.getenv("EXCHANGE_RATE_ACCESS_KEY")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
print(f"✅ APILayer Key Loaded: {AVIATIONSTACK_ACCESS_KEY[:4]}... (hidden)")

# Get root directory of the project
base_dir = os.getcwd() + os.sep
print(f'Base Directory: {base_dir}')

# Directory Paths
DATA_DIR = os.path.join(base_dir, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
RAW_EXCHANGE_RATE_DIR = os.path.join(RAW_DATA_DIR, 'exchange_rates')
RAW_FLIGHT_DATA_DIR = os.path.join(RAW_DATA_DIR, 'flights')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
CONFIG_DIR = os.path.join(base_dir, 'config')
DOCKER_DIR = os.path.join(base_dir, 'docker')
# SCRIPTS_DIR = os.path.join(base_dir, 'scripts')

# Create directories (if not exist)
def create_directories():
    directories = [
        DATA_DIR,
        RAW_DATA_DIR,
        RAW_EXCHANGE_RATE_DIR,
        RAW_FLIGHT_DATA_DIR,
        PROCESSED_DATA_DIR,
        CONFIG_DIR,
        DOCKER_DIR,
        # SCRIPTS_DIR
    ]

    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f'Created directory: {directory}')
        else:
            print(f'Directory exists: {directory}')

# Load Config Function
def load_config(filename='settings.yaml'):
    config_file = os.path.join(CONFIG_DIR, filename)
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

# Run main
if __name__ == '__main__':
    create_directories()

    config = load_config()
    print(f'Loaded config: {config}')

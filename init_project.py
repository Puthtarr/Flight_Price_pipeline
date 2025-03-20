import os
from settings import *

def create_directories():
    directories = [
        DATA_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        DOCKER_DIR,
        CONFIG_DIR
    ]

    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f'Created directory: {directory}')
        else:
            print(f'Already Exist: {directory}')

if __name__ == '__main__':
    create_directories()
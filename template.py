import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "YOUR_PROJECT_NAME"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/_init_.py",
    f"src/components/_init.py", 
    f"src/utils/__init_.py",
    f"src/config/_init_.py",
    f"src/config/configuration.py",
    f"src/pipeline/_init_.py",
    f"src/entity/_init_.py",
    f"src/constants/_init_.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "notebooks/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory, {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")

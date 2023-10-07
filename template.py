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
    "research/trials.ipynb",
    "templates/index.html",
]

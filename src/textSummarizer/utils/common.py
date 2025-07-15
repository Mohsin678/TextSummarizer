import os
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any
from src.textSummarizer.logging import logger
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml,"w") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"loaded successfully {path_to_yaml} file")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
def create_directories(path_to_directories:list, verbose=True):
    for path in create_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")
    
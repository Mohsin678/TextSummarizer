from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfg:
    root_dir:Path
    source_url:Path
    local_data_file:Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_Path:Path
    model_ckpt:Path
    num_train_epochs:int
    warmup_steps:int
    per_device_train_batch_size:int
    weight_decay:float
    logging_steps:int
    evaluation_strategy:str
    eval_steps:int
    save_steps:float
    gradient_accumulation_steps:int
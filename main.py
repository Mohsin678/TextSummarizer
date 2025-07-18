from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion import DataInestionPipeline
from src.textSummarizer.pipeline.data_transformation import DataTransformationPipeline
from src.textSummarizer.pipeline.model_trainer import ModelTrainerPipeline



stage_name = "data ingestion stage"
try:
    logger.info(f"stage{stage_name} initiated")
    data_ingestion = DataInestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"stage{stage_name} completed")
except Exception as e:
    raise e


stage_name = "data Transformation stage"
try:
    logger.info(f"stage{stage_name} initiated")
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f"stage{stage_name} completed")
except Exception as e:
    raise e

stage_name = "Model Trainer stage"
try:
    logger.info(f"stage{stage_name} initiated")
    Model_trainer = ModelTrainerPipeline()
    Model_trainer.initiate_model_trainer()
    logger.info(f"stage{stage_name} completed")
except Exception as e:
    raise e
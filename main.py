from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.data_ingestion import DataInestionPipeline


stage_name = "data ingestion stage"
try:
    logger.info(f"stage{stage_name} initiated")
    data_ingestion = DataInestionPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"stage{stage_name} completed")
except Exception as e:
    raise e
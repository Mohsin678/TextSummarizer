from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer.logging import logger

class DataInestionPipeline:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion =DataIngestion(config = data_ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
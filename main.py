from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

def run_pipeline_stage(stage_name, pipeline_class):
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline = pipeline_class()
        pipeline.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    # Running Data Ingestion stage
    STAGE_NAME = "Data Ingestion stage"
    run_pipeline_stage(STAGE_NAME, DataIngestionTrainingPipeline)
    
    # Running Prepare Base Model stage
    STAGE_NAME = "Prepare base model"
    run_pipeline_stage(STAGE_NAME, PrepareBaseModelTrainingPipeline)
    
    # Running Training stage
    STAGE_NAME = "Training"
    run_pipeline_stage(STAGE_NAME, ModelTrainingPipeline)
    
    # Running Evaluation stage
    STAGE_NAME = "Evaluation stage"
    run_pipeline_stage(STAGE_NAME, EvaluationPipeline)
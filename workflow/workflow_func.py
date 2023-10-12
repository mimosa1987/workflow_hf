from utils.class_func import get_cls
from utils.reflection import Reflection
import sys
import logging
import transformers

logger = logging.getLogger(__name__)


def set_job_log(job_logger, train_args):
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(levelno)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    if train_args.should_log:
        # The default of training_args.log_level is passive, so we set log level at info here to have that default.
        transformers.utils.logging.set_verbosity_info()
    log_level = train_args.get_process_log_level()
    job_logger.setLevel(log_level)
    transformers.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.enable_default_handler()
    transformers.utils.logging.enable_explicit_format()


def get_args(workflow_config):
    model_arguments_cls, data_arguments_cls, training_arguments_cls = _get_args_from_config(workflow_config)
    return model_arguments_cls, data_arguments_cls, training_arguments_cls


def _get_args_from_config(workflow_cls_config):
    model_args_conf = workflow_cls_config.get('args').get('model_args')
    data_args_conf = workflow_cls_config.get('args').get('data_args')
    train_args_conf = workflow_cls_config.get('args').get('train_args')
    logger.info(
        f"Model arguments class : {model_args_conf} \n "
        f"Data arguments class : {data_args_conf} \n "
        f"Train arguments class :{train_args_conf} \n")
    model_arguments_cls = get_cls(model_args_conf)
    data_arguments_cls = get_cls(data_args_conf)
    training_arguments_cls = get_cls(train_args_conf)
    return model_arguments_cls, data_arguments_cls, training_arguments_cls


def get_input_dataset_class(workflow_cls_config):
    dataset_conf = workflow_cls_config.get('data').get('input_data_class')
    dataset_cls = get_cls(dataset_conf)
    return dataset_cls


def load_prompt(workflow_cls_config):
    pass

def load_tokenizer(workflow_cls_config):
    pass
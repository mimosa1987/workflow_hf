from utils.class_func import get_cls
import logging

logger = logging.getLogger(__name__)


def get_args_class(workflow_config):
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
    logger.info(
        f"Input dataset arguments class : {dataset_conf} \n ")
    return dataset_cls


def get_prompt_class(workflow_cls_config):
    prompt_conf = workflow_cls_config.get('data').get('prompt_class')
    prompt_cls = get_cls(prompt_conf)
    return prompt_cls


def get_tokenizer_class(workflow_cls_config):
    tokenize_conf = workflow_cls_config.get('data').get('tokenizer_class')
    tokenize_cls = get_cls(tokenize_conf)
    return tokenize_cls

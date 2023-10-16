#!/usr/bin/env python
# coding=utf-8
import json
import os
import sys
import logging
from workflow.wf_func import (
    set_job_log
)

from workflow.wf_cls import (
    get_args_class,
    get_prompt_class,
    get_tokenizer_class,
    get_input_dataset_class,
)

from transformers import (
    HfArgumentParser,
    set_seed,
)

logger = logging.getLogger(__name__)


def run():
    # get work job config from wf_config_file
    wf_cls_config_file = 'config/class.json'

    with open(wf_cls_config_file, 'r') as f:
        wf_cls_config = f.read()
    workflow_cls_config = json.loads(wf_cls_config)
    logger.info(f"WorkFlow config : {workflow_cls_config}")

    # 获取作业参数配置
    model_arguments_cls, data_arguments_cls, training_arguments_cls = get_args_class(workflow_cls_config)
    parser = HfArgumentParser((model_arguments_cls, data_arguments_cls, training_arguments_cls))

    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        model_args, data_args, training_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[1]))
    else:
        model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    # 初始化log
    set_job_log(logger, training_args)
    logger.info(f"Model arguments : {model_args} \n "
                f"Data arguments : {data_args} \n "
                f"Train arguments : {training_args} \n"
                )

    import socket
    logger.warning(
        f"Host: {socket.gethostname()}, Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
        + f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
    )
    # 为了可以复现训练过程
    set_seed(training_args.seed)

    # 加载数据集
    # 获取 prompter 和 tokenizer
    # prompt_cls = get_prompt_class()
    tokenizer_cls = get_tokenizer_class(workflow_cls_config)

    data_cls = get_input_dataset_class(workflow_cls_config)
    data = data_cls(
        data_args=data_args,
        model_args=model_args,
        # ptompt_cls=prompt_cls,
        tokenizer_cls=tokenizer_cls
    ).load()
    print(data)

#   # 加载 Config
#   model_config = get_config(model_args)
#
#   # 检查checkpoint
#   is_exist_checkpoint, checkpoint = check_and_get_checkpoint()
#
#   # 加载模型
#   model = get_model(model_args, model_config, job_type)
#   if need_load_checkpint_first and is_exist_checkpoint:
#       load_checkpoint(checkpoint)
#
#   # 模型包装 由训练方式决定
#   model = get_wrap_model(model, job_type, model_args)
#
#   # 输入数据处理，输出生成data collator
#   data_collator  = get_data_collator(prompt, tokenizer, preprocess_train, preprocess_eval, preprocess_test, data_args)
#
#   # Initialize Trainer
#   trainer = initialize_train(model, training_args, data, tokenizer, data_collator, **wargs)
#   # Training
#   if training_args.do_train:
#       do_train(trainer)
#   if training_args.do_eval:
#       do_eval(trainer)
#   # Predict
#   if training_args.do_predict:
#       do_predict(trainer)
# #   return results


if __name__ == "__main__":
    run()

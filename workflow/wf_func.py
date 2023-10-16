import sys
import logging
import transformers

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
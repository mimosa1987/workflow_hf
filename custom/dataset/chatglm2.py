import glob

from transformers import AutoTokenizer

from base.dataset import BaseDataSet


class ChatGLM2DataSet(BaseDataSet):
    def __init__(self, data_args, model_args):
        super().__init__(data_args, model_args)

    def init_tokenizer(self):
        if self.model_args.tokenizer_name is not None:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_args.tokenizer_name, trust_remote_code=True)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_args.model_name_or_path, trust_remote_code=True)

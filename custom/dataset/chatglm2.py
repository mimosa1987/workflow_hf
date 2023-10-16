from transformers import AutoTokenizer

from base.dataset import BaseDataSet

class ChatGLM2DataSet(BaseDataSet):
    def __init__(self, data_args, model_args, tokenizer_cls=None, prompt_cls=None):
        super().__init__(data_args, model_args, tokenizer_cls, prompt_cls)

    def init_tokenizer(self):
        tokenizer_name = self.model_args.tokenizer_name \
            if self.model_args.tokenizer_name is not None \
            else self.model_args.model_name_or_path
        self.tokenizer = self.tokenizer_cls.from_pretrained(tokenizer_name, trust_remote_code=True)

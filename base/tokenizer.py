class BaseTokenizer:
    def __init__(
            self,
            tokenizer_name_or_path,
    ):
        self.tokenizer_name_or_path = tokenizer_name_or_path

    def _pre_tokeinze(self):
        pass

    def tokenize(self):
        self._pre_tokeinze()
        # tokenize
        self._post_tokenize()
        pass

    def _post_tokenize(self):
        pass
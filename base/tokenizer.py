from abc import abstractmethod

from transformers import PreTrainedTokenizer


class BaseTokenizer(PreTrainedTokenizer):
    def __init__(self, padding_side='left', **kwargs):
        super().__init__(padding_side=padding_side, **kwargs)

    @abstractmethod
    def _pre_tokenize(self):
        pass

    def tokenize_plus(self, text, **kwargs):
        self._pre_tokenize()
        # tokenize
        self.tokenize(text, **kwargs)
        self._post_tokenize()

    @abstractmethod
    def _post_tokenize(self):
        pass

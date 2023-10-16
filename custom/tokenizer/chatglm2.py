from base.tokenizer import BaseTokenizer

# 需要测试下非AutoTokenizer
class ChatGLM2Tokenizer(BaseTokenizer):
    def __init__(self, padding_side='left', **kwargs):
        super().__init__(padding_side=padding_side, **kwargs)

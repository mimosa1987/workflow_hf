import glob
import os.path
from datasets import load_dataset
from transformers import AutoTokenizer


class BaseDataSet:
    def __init__(self, data_args, model_args, tokenizer_cls=None, prompt_cls=None):
        self.train_files = None
        self.eval_files = None
        self.test_files = None
        self.data_args = data_args
        self.model_args = model_args
        self.has_test = False
        if tokenizer_cls is None:
            self.tokenizer_cls = AutoTokenizer
        else:
            self.tokenizer_cls = tokenizer_cls
        self.tokenizer = None
        self.init_tokenizer()

        if prompt_cls is None:
            self.init_prompt()
        else:
            self.prompt_cls = prompt_cls

    def init_tokenizer(self):
        tokenizer_name = self.model_args.tokenizer_name \
            if self.model_args.tokenizer_name is not None \
            else self.model_args.model_name_or_path
        self.tokenizer = self.tokenizer_cls.from_pretrained(tokenizer_name)

    def init_prompt(self):
        pass

    def _pre_load(self):
        # 判断
        if self.model_args.data_dir is not None:
            self.load_type = 'dir'

    def load(self):
        self._pre_load()
        # 数据集梳理过程
        # 1、加载数据集
        # code for load data
        if self.load_type == 'dir':
            data = self.load_data_from_directory()

        # 2、prompt 处理
        # code for prompt
        data = self.prompt(data)
        # 3、tokenizer 处理
        # code for tokenizer
        data = self.tokenizer(data)

        self._post_load()
        return data

    def _post_load(self):
        pass

    def _check_dir(self, path_name):
        if not os.path.isdir(path_name):
            raise ValueError(f"{path_name} must be a folder!")
        if not os.path.exists(os.path.join(path_name, 'train')) or len(
                os.listdir(os.path.join(path_name, 'train'))) == 0:
            raise ValueError(
                f"There must be at least the train folder under the {path_name} folder and train folder must not be EMPTY!")
        if not os.path.exists(os.path.join(path_name, 'eval')) or len(os.listdir(os.path.join(path_name, 'eval'))) == 0:
            raise ValueError(
                f"There must be at least the eval folder under the {path_name} folder and eval folder must not be EMPTY!")
        if os.path.exists(os.path.join(path_name, 'test')):
            return True
        return False

    def load_data_from_directory(self):
        if self.data_args.data_dir is not None:
            self.has_test = self._check_dir(self.data_args.data_dir)
            train_dir = os.path.join(self.data_args.data_dir, 'train')
            eval_dir = os.path.join(self.data_args.data_dir, 'eval')
            self.train_files = glob.glob("%s/**" % train_dir)
            self.eval_files = glob.glob("%s/**" % eval_dir)
            if self.has_test:
                test_dir = os.path.join(self.data_args.data_dir, 'test')
                self.test_files = glob.glob("%s/**" % test_dir)
            ext = self.train_files[0].split('.')[-1]
            if self.has_test:
                return load_dataset(
                    ext,
                    data_files={"train": self.train_files, "eval": self.eval_files, "test": self.test_files},
                    cache_dir=self.model_args.cache_dir if self.data_args.data_cache_dir is None else self.data_args.data_cache_dir,
                    use_auth_token=True if self.model_args.use_auth_token else None,
                )
            else:
                return load_dataset(
                    ext,
                    data_files={"train": self.train_files, "eval": self.eval_files, "test": self.test_files},
                    cache_dir=self.model_args.cache_dir,
                    use_auth_token=True if self.model_args.use_auth_token else None,
                )

import glob
import random


class BaseDataSet():
    def __init__(self):
        pass

class DirectoryDataSet(BaseDataSet):
    def __init__(self):
        super().__init__()

    def get_data(self, pathname, split = 'train', k = 10):
        file_list = glob(pathname)
        ext = file_list[0].split('.')[-1]
        if split == 'all':
            test_files = random.sample(file_list, k=k)
            train_file = [i for i in file_list if i not in test_files]
            return ext, {"train" : train_file, "valid" : test_files }
        else:
            return  ext, {split : file_list}


import importlib
import os.path
import sys

from utils.reflection import Reflection


def get_cls(cls_dic):
    if os.path.isfile(cls_dic.get('module')):
        dir_name = os.path.dirname(cls_dic.get('module'))
        sys.path.append(dir_name)
        filename = os.path.basename(cls_dic.get('module'))
        module = importlib.import_module(filename.split('.')[0])
        class_name = cls_dic.get("class")
        if hasattr(module, class_name):
            obj_cls = getattr(module, class_name)
            return obj_cls
    else:
        module_name = cls_dic.get('module')
        class_name = cls_dic.get('class')
        return Reflection.reflect_cls(module_name, class_name)

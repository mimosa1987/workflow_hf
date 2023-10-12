# -*- coding: utf-8 -*-
###
# author: zhaolihan
# date	: 20230914
###
import importlib
import importlib.util

class Reflection(object):
    @staticmethod
    def reflect_obj(module_path, class_name, params = None):
        module = importlib.import_module(module_path)
        if hasattr(module, class_name):
            obj_cls = getattr(module, class_name)
            if params is None or params == "":
                return obj_cls()
            else:
                return obj_cls(**params)
        else:
            raise AttributeError('%s Not have class %s in it!' % (module_path, class_name))

    @staticmethod
    def reflect_cls(module_path, class_name):
        import os
        if os.path.isfile(module_path):
            module_spec = importlib.util.spec_from_file_location('reflection_module', module_path)
            reflection_module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(reflection_module)
            module = reflection_module
        else:
            module = importlib.import_module(module_path)
        if hasattr(module, class_name):
            obj_cls = getattr(module, class_name)
            return obj_cls

    @staticmethod
    def reflect_func(class_obj, func_name):
        if hasattr(class_obj, func_name):
            func = getattr(class_obj, func_name)
            return func
        else:
            raise AttributeError('%s Not have class %s in it!' % (class_obj, func_name))

    @staticmethod
    def reflect_obj_func(module_path, func_name):
        module = importlib.import_module(module_path)
        if hasattr(module, func_name):
            func = getattr(module, func_name)
            return func

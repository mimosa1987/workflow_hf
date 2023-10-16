from workflow.wf_cls import _get_cls

class_dict = {"module" : "/Users/zhaolihan/Documents/personal/practice/dev/workflow_hf/custom/arguments/chatglm2.py", "class" : "CustomModelArguments"}
a = _get_cls(class_dict)
print(a)
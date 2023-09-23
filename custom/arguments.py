from dataclasses import dataclass, field
from typing import Optional, Dict, Optional, Union
from ampha.base.arguments import ModelArguments, DataTrainingArguments


@dataclass
class CustomModelArguments(ModelArguments):
    def __init__(self):
        super().__init__()


@dataclass
class CustomDataTrainingArguments(DataTrainingArguments):
    def __init__(self):
        super().__init__()
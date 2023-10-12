from dataclasses import dataclass, field
from typing import Optional, Dict, Optional, Union
from base.arguments import ModelArguments, DataArguments


@dataclass
class CustomModelArguments(ModelArguments):
    custom_model_args: Optional[str] = field(
        default=None, metadata={"help": "The name of the dataset to use (via the datasets library)."}
    )

@dataclass
class CustomDataArguments(DataArguments):
    custom_data_args: Optional[str] = field(
        default=None, metadata={"help": "The name of the dataset to use (via the datasets library)."}
    )

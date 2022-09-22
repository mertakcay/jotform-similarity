from pydantic import BaseModel
from typing import Optional, List


class formModel(BaseModel):
    SimilarForm: List[int]
    Probability:List[float]
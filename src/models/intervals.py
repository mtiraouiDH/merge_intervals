from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator

class Interval(BaseModel):
    start: int = Field(description="Start Range of an interval")
    end: int = Field(description="End Range of an interval")

class IntervalSet(BaseModel):
    includes: List[Interval] = Field(default=None, description="Set of include intervals")
    excludes: List[Interval] = Field(default=None, description="Set of exclude intervals")

    @model_validator(mode='after')
    def check_interval_sets(self) -> 'IntervalSet':
        inc = self.includes
        exc = self.excludes
        if inc is None:
            raise ValueError('includes array must be provided')
        if exc is None:
            raise ValueError('excludes array must be provided')
        return self

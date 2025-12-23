from pydantic import BaseModel
from datetime import time

class Time(BaseModel):
    start: time
    end: time

class DomainRules(BaseModel):
    id: str
    allowed: bool
    domains: list[str]
    time: list[Time]|None

class Rules(BaseModel):
    mode: int #1: No Restrictions, 2: Restricted mode 3: No access
    rules: list[DomainRules]
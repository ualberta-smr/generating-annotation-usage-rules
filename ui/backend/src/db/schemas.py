from pydantic import BaseModel

class CandidateRule(BaseModel):
    id: int
    antecedent: str
    consequent: str
    package_id: int

    class Config:
        orm_mode = True


class CandidateRulesPackage(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True



class LabeledRule(BaseModel):
    id: str
    candidate_rule_id: int
    rule_description: str
    label: str
    user_id: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True

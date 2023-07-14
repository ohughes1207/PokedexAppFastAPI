from pydantic import BaseModel, validator

class VariantCreateRequest(BaseModel):
    pokedex_num: int
    var_name: str
    type_1: str
    type_2: str
    total_stats: int
    hp: int
    att: int
    defense: int
    sp_att: int
    sp_def: int
    speed: int
    regional: bool
    mega: bool
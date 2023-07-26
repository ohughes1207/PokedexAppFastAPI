from pydantic import BaseModel, validator

class PokemonCreateRequest(BaseModel):
    pokedex_num: int
    base_name: str
    gen: int
    mythical: bool
    legendary: bool
    paradox: bool
    ultrabeast: bool
    pseudo_legendary: bool

    @validator('gen')
    def check_max_gen_characters(cls, v):
        if len([x for x in str(v)]) >= 3:
            raise ValueError('Check generation')
        return v
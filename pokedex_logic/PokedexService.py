from db_configs.models import Pokemon, Variant, Type
from sqlalchemy.orm import joinedload

class PokedexService:
    def __init__(self):
        pass
    def getAllPokemon(self, db):
        pokemon_list = db.query(Pokemon).options(joinedload(Pokemon.variants)).all()
        
    def getAllVariants(self, db):
        return db.query(Variant).all()

    def getAllType(self, db):
        return db.query(Type).all()

    def getPokemonByName(self, pokemon_name : str, db):
        if len(db.query(Pokemon).filter(Pokemon.base_name.ilike(f"%{pokemon_name}%")).all())==0:
            return {'message': 'Pokemon not found!'}
        else:
            return db.query(Pokemon).filter(Pokemon.base_name.ilike(f"%{pokemon_name}%")).all()


    def getAllPokemonPaginated(self, page, db):
        #50 pokemon per page
        limit=50
        count = db.query(Pokemon).count()
        skip = (page - 1) * limit
        total_pages = count / limit if count % limit == 0 else count // limit + 1
        return {"data": db.query(Pokemon).offset(skip).limit(limit).all(), "total": count, "page": page, "per_page": limit, "total_pages": total_pages}
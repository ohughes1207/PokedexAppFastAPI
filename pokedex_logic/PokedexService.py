from db_configs.models import Pokemon, Variant, Type
from sqlalchemy.orm import joinedload
from sqlalchemy import null

class PokedexService:
    def __init__(self):
        pass
    def getAllPokemon(self, db):
        pokemon_list = db.query(Pokemon).options(joinedload(Pokemon.variants)).all()
        return pokemon_list
        
    def getAllVariants(self, db):
        return db.query(Variant).all()

    def getAllType(self, db):
        return db.query(Type).all()

    def getPokemonByName(self, pokemon_name : str, db):
        if len(db.query(Pokemon).filter(Pokemon.base_name.ilike(f"%{pokemon_name}%")).all())==0:
            return {'message': 'Pokemon not found!'}
        else:
            return db.query(Pokemon).filter(Pokemon.base_name.ilike(f"%{pokemon_name}%")).all()

    def getFilteredPokemon(self, pokemon_name : str, T1 : str, T2 : str, genValue : int, Leg : bool, Para : bool, Pseudo : bool, UB : bool, Myth : bool, Regional : bool, Mega : bool, db):
        query = db.query(Pokemon)
        if pokemon_name:
            query = query.filter(Pokemon.base_name.ilike(f"%{pokemon_name}%"))
        if genValue:
            query = query.filter(Pokemon.gen == genValue)
        if Leg:
            query = query.filter(Pokemon.legendary == True)
        if Para:
            query = query.filter(Pokemon.paradox == True)
        if Pseudo:
            query = query.filter(Pokemon.pseudo_legendary == True)
        if UB:
            query = query.filter(Pokemon.ultrabeast == True)
        if Myth:
            query = query.filter(Pokemon.mythical == True)

        query = query.options(joinedload(Pokemon.variants)).all()

        if T1:
            query = query.filter(Pokemon.variants.any(type_1=T1))
        if T2:
            if T2==T1:
                query = query = query.filter(Pokemon.variants.any(type_2=null()))
            else:
                query = query.filter(Pokemon.variants.any(type_2=T2))

        if Regional:
            query = query.filter(Pokemon.variants.any(regional == True))
        if Mega:
            query = query.filter(Pokemon.variants.any(mega == True))

            return query.all()


    def getAllPokemonPaginated(self, page, db):
        #50 pokemon per page
        limit=50
        count = db.query(Pokemon).count()
        skip = (page - 1) * limit
        total_pages = count / limit if count % limit == 0 else count // limit + 1
        return {"data": db.query(Pokemon).offset(skip).limit(limit).all(), "total": count, "page": page, "per_page": limit, "total_pages": total_pages}
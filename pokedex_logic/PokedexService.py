from db_configs.models import Pokemon, Variant, Type
from sqlalchemy import and_, or_
from sqlalchemy.orm import joinedload

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

    def getFilteredPokemon(self, pokemon_name : str, T1 : str, T2 : str, genValue : int, Leg : bool, Para : bool, Pseudo : bool, UB : bool, Myth : bool, Regional : bool, Mega : bool, page : int, db):
        query = db.query(Pokemon)
        if pokemon_name:
            query = query.filter(Pokemon.variants.any(Variant.var_name.ilike(f"%{pokemon_name}%")))
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

        if T1:
            query = query.filter(Pokemon.variants.any(or_(Variant.type_1.ilike(f"%{T1}%"), Variant.type_2.ilike(f"%{T1}%"))))
        if T2:
            if T2==T1:
                query = query.filter(Pokemon.variants.any(and_(Variant.type_1.ilike(f"%{T1}%"), Variant.type_2 == None)))
            elif T1 is not None:
                query = query.filter(Pokemon.variants.any(or_(and_(Variant.type_1.ilike(f"%{T1}%"), Variant.type_2.ilike(f"%{T2}%")), and_(Variant.type_1.ilike(f"%{T2}%"), Variant.type_2.ilike(f"%{T1}%")))))
            else:
                query = query.filter(Pokemon.variants.any(or_(Variant.type_1.ilike(f"%{T2}%"), Variant.type_2.ilike(f"%{T2}%"))))

        if Regional:
            query = query.filter(Pokemon.variants.any(Variant.regional == True))
        if Mega:
            query = query.filter(Pokemon.variants.any(Variant.mega == True))

        limit=50
        count = query.count()
        skip = (page - 1) * limit
        total_pages = count / limit if count % limit == 0 else count // limit + 1
        query = query.offset(skip).limit(limit)

        pokemonData = query.options(joinedload(Pokemon.variants)).all()

        return {"data": pokemonData, "total": count, "page": page, "per_page": limit, "total_pages": total_pages}

    def getAllPokemonPaginated(self, page, db):
        #50 pokemon per page
        limit=50
        count = db.query(Pokemon).count()
        skip = (page - 1) * limit
        total_pages = count / limit if count % limit == 0 else count // limit + 1
        pokemonData = db.query(Pokemon).offset(skip).limit(limit).options(joinedload(Pokemon.variants)).all()
        return {"data": pokemonData, "total": count, "page": page, "per_page": limit, "total_pages": total_pages}

    def getVariantBySearch(self, search, db):
        query = db.query(Variant)
        if search:
            query = query.filter(Variant.var_name.ilike(f"%{search}%"))

            pokemonData = query.options(joinedload(Variant.type_1_rel)).options(joinedload(Variant.type_2_rel)).all()

            return pokemonData
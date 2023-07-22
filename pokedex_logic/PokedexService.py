from db_configs.models import Pokemon, Variant, Type

class PokedexService:
    def __init__(self):
        pass
    def getAllPokemon(self, db):
        return db.query(Pokemon).all()

    def getAllVariants(self, db):
        return db.query(Variant).all()

    def getAllType(self, db):
        return db.query(Type).all()

    def getPokemonByName(self, pokemon_name : str):
        for pokemon in self.pokemonRecords:
            if pokemon['base_name'].lower().__contains__(pokemon_name.lower()):
                return pokemon
        return {'message': 'Pokemon not found!'}


    def getAllPokemonPaginated(self, page, db):
        #50 pokemon per page
        limit=50
        count = db.query(Pokemon).count()
        skip = (page - 1) * limit
        total_pages = count / limit if count % limit == 0 else count // limit + 1
        return {"data": db.query(Pokemon).offset(skip).limit(limit).all(), "total": count, "page": page, "per_page": limit, "total_pages": total_pages}
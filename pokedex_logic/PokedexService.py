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
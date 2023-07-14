class PokedexService:
    def __init__(self):
        pass
    def getAllPokemon(self):
        return self.pokemonRecords

    def getPokemonByName(self, pokemon_name : str):
        for pokemon in self.pokemonRecords:
            if pokemon['base_name'].lower().__contains__(pokemon_name.lower()):
                return pokemon

        return {'message': 'Pokemon not found!'}
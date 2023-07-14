from fastapi import FastAPI, Depends, UploadFile
from pokedex_logic.PokedexService import PokedexService
from db_configs.connection import Base, engine, get_db
from db_configs import models
from sqlalchemy.orm import Session
from db_configs import fileuploads as fu

from schemas.PokemonSchemas import PokemonCreateRequest
from schemas.VariantSchemas import VariantCreateRequest

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello from Olli!'}


@app.get('/pokemon')
def getAllPokemon():
    return PokedexService().getAllPokemon()


@app.get('/pokemon/{pokemon_name}')
def getPokemonByName(pokemon_name : str):
    return PokedexService().getPokemonByName(pokemon_name)


@app.post('/pokemon')
def uploadPokemon(pokemonCSV: UploadFile, db : Session = Depends(get_db)):
    fu.uploadCSVToPokemonDatabase(pokemonCSV, db)
    return {"message": 'File uploaded successfully'}


@app.post('/variants')
def uploadPokemon(pokemonCSV: UploadFile, db : Session = Depends(get_db)):
    fu.uploadCSVToVariantDatabase(pokemonCSV, db)
    return {"message": 'File uploaded successfully'}

@app.post('/types')
def uploadPokemon(pokemonTypesCSV: UploadFile, db : Session = Depends(get_db)):
    fu.uploadCSVToTypeDatabase(pokemonTypesCSV, db)
    return {"message": 'File uploaded successfully'}
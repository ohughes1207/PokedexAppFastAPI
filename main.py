from fastapi import FastAPI, Depends, UploadFile
from pokedex_logic.PokedexService import PokedexService
from db_configs.connection import Base, engine, get_db
from db_configs import models
from sqlalchemy.orm import Session
from db_configs import fileuploads as fu

from schemas.PokemonSchemas import PokemonCreateRequest
from schemas.VariantSchemas import VariantCreateRequest

from origins import origins
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def home():
    return {'message': 'Hello from Olli!'}


@app.get('/pokemon')
def getAllPokemon(db : Session = Depends(get_db)):
    return PokedexService().getAllPokemon(db)


@app.get('/variants')
def getAllVariants(db : Session = Depends(get_db)):
    return PokedexService().getAllVariants(db)


@app.get('/types')
def getAllTypes(db : Session = Depends(get_db)):
    return PokedexService().getAllType(db)


@app.get('/pokemon/search')
def getPokemonByName(pokemon_name : str = '', db : Session = Depends(get_db)):
    return PokedexService().getPokemonByName(pokemon_name, db)


@app.get('/pokemon/filter')
def getFilteredPokemon(
    pokemon_name : str = '',
    T1 : str = '',
    T2 : str = '',
    genValue : int = '',
    Leg : bool = False,
    Para : bool = False,
    Pseudo : bool = False,
    UB : bool = False,
    Myth : bool = False,
    Regional : bool = False,
    Mega : bool = False,
    db : Session = Depends(get_db)):

    return PokedexService().getFilteredPokemon(pokemon_name, T1, T2, genValue, Leg, Para, Pseudo, UB, Myth, Regional, Mega, db)


@app.post('/pokemon')
def uploadPokemon(pokemonCSV: UploadFile, db : Session = Depends(get_db)):
    try:
        fu.uploadCSVToPokemonDatabase(pokemonCSV, db)
    finally:
        return {"message": 'File uploaded successfully'}


@app.post('/variants')
def uploadPokemon(pokemonCSV: UploadFile, db : Session = Depends(get_db)):
    try:
        fu.uploadCSVToVariantDatabase(pokemonCSV, db)
    finally:
        return {"message": 'File uploaded successfully'}

@app.post('/types')
def uploadPokemon(pokemonTypesCSV: UploadFile, db : Session = Depends(get_db)):
    try:
        fu.uploadCSVToTypeDatabase(pokemonTypesCSV, db)
    finally:
        return {"message": 'File uploaded successfully'}
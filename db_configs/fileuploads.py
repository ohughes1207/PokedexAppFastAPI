import csv
from db_configs.models import Pokemon, Variant, Type
from distutils.util import strtobool

def uploadCSVToPokemonDatabase(file, db):

    fileContent = file.file.read().decode('utf-8')

    rows  = csv.reader(fileContent.splitlines(), delimiter=",")
    next(rows)
    existing_pokedex_nums = set()

    for row in rows:
        if row[0] not in existing_pokedex_nums: #or db.query(Pokemon).filter_by(pokedex_num=row[0]).first() is None:
            pokemon = Pokemon(pokedex_num=row[0], base_name=row[1], gen=row[12], legendary=strtobool(row[15]),
            paradox=strtobool(row[14]), pseudo_legendary=strtobool(row[16]), ultrabeast=strtobool(row[17]), mythical=strtobool(row[19]))
            db.add(pokemon)
            existing_pokedex_nums.add(pokemon.pokedex_num)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        


def uploadCSVToVariantDatabase(file, db):

    fileContent = file.file.read().decode('utf-8')

    rows  = csv.reader(fileContent.splitlines(), delimiter=",")
    next(rows)

    for row in rows:

        variant = Variant(pokedex_num=row[0], var_name=row[2], type_1=row[3], type_2=row[4] if row[4] else None, total_stats=row[5],
        hp=row[6], att=row[7], defense=row[8], sp_att=row[9], sp_def=row[10], speed=row[11], regional=strtobool(row[18]), mega=strtobool(row[13]), img_name=row[20])
        db.add(variant)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)


def uploadCSVToTypeDatabase(file, db):

    fileContent = file.file.read().decode('utf-8')

    rows  = csv.reader(fileContent.splitlines(), delimiter=",")
    next(rows)

    for row in rows:
        typesStats = Type(type_name=row[0], def_vs_Grass=row[1], def_vs_Fire=row[2], def_vs_Water=row[3], def_vs_Bug=row[4], def_vs_Normal=row[5], def_vs_Dark=row[6], def_vs_Poison=row[7],
        def_vs_Electric=row[8], def_vs_Ground=row[9], def_vs_Ice=row[10], def_vs_Fairy=row[11], def_vs_Steel=row[12], def_vs_Fighting=row[13], def_vs_Psychic=row[14], def_vs_Rock=row[15],
        def_vs_Ghost=row[16], def_vs_Dragon=row[17], def_vs_Flying=row[18])
        db.add(typesStats)
    try:
        db.commit()
    except:
        db.rollback()
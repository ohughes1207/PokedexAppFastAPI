from sqlalchemy import Column, Integer, String, Boolean, Float, Table, ForeignKey
from db_configs.connection import Base
from sqlalchemy.orm import relationship

class Pokemon(Base):
    __tablename__ = "pokemon_base"
    base_id = Column(Integer, primary_key=True, index=True)
    pokedex_num = Column(Integer, unique=True)
    base_name = Column(String)
    gen = Column(Integer)
    legendary = Column(Boolean)
    paradox = Column(Boolean)
    pseudo_legendary = Column(Boolean)
    ultrabeast = Column(Boolean)
    mythical = Column(Boolean)
    variants = relationship('Variant', backref='pokemon')

class Variant(Base):
    __tablename__ = "variants"
    var_id = Column(Integer, primary_key=True, index=True)
    pokedex_num = Column(Integer, ForeignKey('pokemon_base.pokedex_num'))
    var_name = Column(String, unique=True)
    type_1 = Column(String, ForeignKey('types.type_name'))
    type_2 = Column(String, ForeignKey('types.type_name'), nullable=True)
    total_stats = Column(Integer)
    hp = Column(Integer)
    att = Column(Integer)
    defense = Column(Integer)
    sp_att = Column(Integer)
    sp_def = Column(Integer)
    speed = Column(Integer)
    regional = Column(Boolean)
    mega = Column(Boolean)
    img_name = Column(String)
    type_1_rel = relationship('Type', foreign_keys=[type_1])
    type_2_rel = relationship('Type', foreign_keys=[type_2])



class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True, index=True)
    type_name = Column (String, unique=True)
    def_vs_Grass = Column(Float)
    def_vs_Fire = Column(Float)
    def_vs_Water = Column(Float)
    def_vs_Bug = Column(Float)
    def_vs_Normal = Column(Float)
    def_vs_Dark = Column(Float)
    def_vs_Poison = Column(Float)
    def_vs_Electric = Column(Float)
    def_vs_Ground = Column(Float)
    def_vs_Ice = Column(Float)
    def_vs_Fairy = Column(Float)
    def_vs_Steel = Column(Float)
    def_vs_Fighting = Column(Float)
    def_vs_Psychic = Column(Float)
    def_vs_Rock = Column(Float)
    def_vs_Ghost = Column(Float)
    def_vs_Dragon = Column(Float)
    def_vs_Flying = Column(Float)
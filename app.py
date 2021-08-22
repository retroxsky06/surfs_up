# import dependencies,SQLAlchemy dependencies: help access SQLite
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#create database engine- access the SQLite database
engine = create_engine("sqlite://hawaii.sqlite")

#reflect the database into classes
Base = automap_base()

#refelct the database in SQLAlchemy - save references to each table
Base.prepare(engine, reflect=True)

#Assign variables
Measurement = Base.classes.measurement
Station = Base.classes.station 

#create session link from Py to database
session = Session(engine)

# Set up Flask
app = Flask(__name__)
@app.route('/')
def welcome():
    return(
    '''   
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/emd
    ''')

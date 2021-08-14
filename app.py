# INITIAL FLASK APPLICATION

# from flask import Flask

# # New flask instance
# app = Flask(__name__)

# # Define starting point
# @app.route('/')
# def hello_world():
#     return 'Hello world'

# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create engine for SQLite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Create references to classes for easy reference
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create link from Python to Database
session = Session(engine)

# Set Up Flask
app = Flask(__name__)

# Create the welcome route with links to other routes
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create the Precipitation route
@app.route("/api/v1.0/precipitation")

def precipitation():

    # Calculate date 1 year ago from most recent date in DB
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query to pull precipitation data and prcp into variable for filter
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()

    # Prep for jsonification
    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)

# Create the stations route
@app.route("/api/v1.0/stations")

def stations():
    
    # Query to get all the stations
    results = session.query(Station.station).all()

    # Unravel results into 1 dimensional array and then convert to list
    stations = list(np.ravel(results))

    # Set stations key in JSON equal to json list and return jsonified 
    return jsonify(stations=stations)

# Create the temperature observations route
@app.route("/api/v1.0/tobs")

def temp_monthly():

    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    # Unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))

    # Set stations key in JSON equal to json list and return jsonified 
    return jsonify(temps=temps)

# Provide both a starting and ending date for routes
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):

    # Query to select the minimum, average, and maximum temperatures
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

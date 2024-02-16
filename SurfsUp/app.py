# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    year_precipitation = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date).filter(Measurement.date >= year_precipitation).all()
    clean_data = {}
    for row in precipitation_data:
        clean_data[row[0]] = row[1]
    session.close()
    return jsonify(clean_data)



@app.route("/api/v1.0/stations")
def stations():
    #code goes here
    return 'jsonify "stations"'

@app.route("/api/v1.0/tobs")
def tobs():
    #code goes here
    return 'jsonify "tobs"'


if __name__ == "__main__":
    app.run(debug=True)
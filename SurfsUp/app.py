# Import the dependencies.
from flask import Flask, jsonify


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
    #code goes here
    my_list = [5, 75, 389]
    return jsonify(my_list)

@app.route("/api/v1.0/stations")
def stations():
    #code goes here
    return jsonify "stations"

@app.route("/api/v1.0/tobs")
def tobs():
    #code goes here
    return jsonify "tobs"


if __name__ == "__main__":
    app.run(debug=True)
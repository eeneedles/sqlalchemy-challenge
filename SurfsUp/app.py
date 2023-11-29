# Import the dependencies.
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app=Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return "Flask is not so bad"

@app.route("/api/v1.0/precipitation")
def precipitation():
    #code goes here
    my_list = [5, 75, 389]
    return jsonify(my_list)

@app.route("/api/v1.0/stations")
def stations():
    #code goes here
    return jsonify "stations"

@app.route()
def tobs():
    #code goes here
    return jsonify "tobs"


if __name__ == "__main__":
    app.run(debug=True)
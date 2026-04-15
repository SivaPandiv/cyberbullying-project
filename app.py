from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# DB connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="maps_db"
)

@app.route("/save", methods=["POST"])
def save():
    data = request.json

    start = data["start"]
    end = data["end"]
    vehicle = data["vehicle"]

    cursor = db.cursor()
    query = "INSERT INTO routes (start, end, vehicle) VALUES (%s, %s, %s)"
    values = (start, end, vehicle)

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Saved successfully"})

if __name__ == "__main__":
    app.run(debug=True)
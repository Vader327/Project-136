from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success",
    })

@app.route("/star_data")
def star_data():
    name = request.args.get("name")

    try:
        final = next(item for item in data if item["name"] == name)
        message = "success"
        
    except Exception as e:
        print(e)
        final = "Could not find star " + name
        message = "failure"
        
    return jsonify({
        "data": final,
        "message": message,
    })

if __name__ == "__main__":
    app.run(debug=True)

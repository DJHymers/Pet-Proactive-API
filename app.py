import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def handle_post_request():
    data = request.get_json()

    if data and data.get("command") == "greeting" and data.get("name"):
        name = data["name"]
        response_data = {"response": f"hello {name}"}
        return json.dumps(response_data), 200, {"Content-Type": "application/json"}
    else:
        return "Forbidden", 403


if __name__ == "__main__":
    app.run()

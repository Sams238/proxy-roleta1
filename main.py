
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/dados")
def proxy_roleta():
    try:
        url = "https://api.casinoscores.com/svc-evolution-game-events/api/xxxtremelightningroulette/latest"
        headers = {
            "accept": "application/json, text/plain, */*",
            "origin": "https://casinoscores.com",
            "referer": "https://casinoscores.com/",
            "user-agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

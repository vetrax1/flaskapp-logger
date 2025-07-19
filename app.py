from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route("/")
def log_request():
    log = f"Request received at {datetime.datetime.now()}"
    print(log)
    return log

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
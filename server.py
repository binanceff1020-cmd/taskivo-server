from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Taskivo server is running!"


@app.route("/offerwall/postback", methods=["POST", "GET"])
def offerwall_postback():

    data = request.form.to_dict()

    if not data:
        data = request.args.to_dict()

    print("Offerwall Postback Received:")
    print(data)

    return "OK", 200


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))

    app.run(
        host="0.0.0.0",
        port=port
    )

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from commands import *
from listener import listen

from controller import JarvisController
from system import get_system_info

app = Flask(__name__)
CORS(app)

controller = JarvisController()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "")

    answer = controller.process(message)

    return jsonify({
        "reply": answer
    })

@app.route("/command", methods=["POST"])
def command():

    data = request.get_json()

    cmd = data.get("command", "").lower()

    try:

        if cmd == "google":
            open_google()

        elif cmd == "youtube":
            open_youtube()

        elif cmd == "calculator":
            open_calculator()

        elif cmd == "notepad":
            open_notepad()

        elif cmd == "explorer":
            open_explorer()

        elif cmd == "cmd":
            open_cmd()

        else:
            return jsonify({
                "success": False,
                "message": "Unknown command"
            })

        return jsonify({
            "success": True
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


@app.route("/system")
def system():

    return jsonify(
        get_system_info()
    )

@app.route("/listen", methods=["POST"])
def listen_route():

    try:

        text = listen()

        return jsonify({
            "success": True,
            "text": text
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )

# from flask import Flask, render_template, subprocess
# import os

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/run_game")
# def run_game():
#     # Ensure game1 folder is in the same directory as server.py
#     game_path = os.path.join(os.path.dirname(__file__), "game1")
#     subprocess.call(["python", "-u", os.path.join(game_path, "main.py")])
#     return "Game Started!"

# if __name__ == "__main__":
#     app.run(debug=True)
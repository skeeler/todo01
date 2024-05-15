from flask import Flask, render_template, request, redirect, url_for

import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
todo_file = os.path.join(basedir, 'todo_list.txt')

todo_list = []

#
# F2-U2 Step 1
# https://github.com/microsoft/EveryoneCanCode-US/blob/main/Track_1_ToDo_App/Sprint-01%20-%20Basic%20Application/Feature%202%20-%20Save%20To-Do%20List/User%20Story%202%20-%20Load%20To-Do%20List%20from%20File.md#updating-the-code-base-for-new-functionality
#

# load the to-do list from a file
try:
    with open(todo_file, "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    print("No existing to-do list found.")

@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form["todo"]
    todo_list.append(todo)
    save_todo_list()
    return redirect(url_for("index"))

def save_todo_list():
    with open(todo_file, "w") as file:
        for todo in todo_list:
            file.write(todo + "\n")

@app.route("/remove", methods=["POST"])
def remove_todo():
    item_number = int(request.form["item_number"])
    if 0 < item_number <= len(todo_list):
        todo_list.pop(item_number - 1)
        save_todo_list()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


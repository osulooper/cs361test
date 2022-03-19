# Nicholas Tucker's Final Project for 361

# This part of the project is an app that will take input from a text box in a GUI. Once submitted,
# the text will be saved into a directory with sub directories for the year and month.

# I had the idea to make a journalling app but I hadn't considered saving the journal on a local machine in directories
# until I saw the video "JOURNAL | Useful Python Projects 02" by Practical Programming on Youtube.

from flask import Flask, render_template, redirect, request
import os
from datetime import date
import subprocess
import time

readable_ts = time.localtime()
time_stamp = (time.strftime("%a - %x %X %Z", readable_ts))
day = date.today().strftime("%d")
year = date.today().strftime("%Y")
month = date.today().strftime("%B")

memories_dir = "Memories"
message = f"Memories for {day} {month}, {year}:"
application = "notepad.exe"


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/my-link/', methods=['GET', 'POST'])
def my_link():
    global memories_dir, message
    memory = request.form['memories']
    message += memory
    memories_absolute_path = get_memories_absolute_path()
    target_dir = get_target_dir(memories_absolute_path)
    go_to_dir(target_dir)
    create_new_entry()
    print("memory created at " + time_stamp)
    return render_template('success.html')


# def main():
#     global memories_dir, message
#
#     memories_absolute_path = get_memories_absolute_path()
#     target_dir = get_target_dir(memories_absolute_path)
#     go_to_dir(target_dir)
#     create_new_entry()

def get_memories_absolute_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir,memories_dir)

def get_target_dir(memories_absolute_path):

    target_dir = os.path.join(memories_absolute_path, year, month)
    return target_dir


def go_to_dir(target_dir):
    try:
        os.makedirs(target_dir)
    except:
        pass
    os.chdir(target_dir)

def create_new_entry():
    filename = f"{month}-{day}-{year}.txt"

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(message)

    subprocess.Popen([application, filename])

if __name__ == '__main__':
    app.run(debug=True)

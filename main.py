from flask import Flask, render_template, send_from_directory, redirect, url_for
import os
import json

app = Flask(__name__, static_url_path = "", static_folder = "static", template_folder = "templates")

class Skill():

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

def read_skills():
    skills = []
    with open("skills.txt", "r", encoding = "utf-8") as f:
        for i in f.readlines():
            try:
                float(i.split(";")[1])
                skills.append(Skill(i.split(";")[0], f"{i.split(';')[1]} of 5 ⭐"))
            except:
                skills.append(Skill(i.split(";")[0], f"{i.split(';')[1]}"))
    return skills

@app.route("/")
def index():
    return render_template("index.html", skills = skills)

@app.route("/curriculum_vitae")
def curriculum_vitae():
    return send_from_directory(f"{workingdir}/static/pdf/", "curriculum_vitae.pdf")

@app.route("/skills", methods = ['GET',])
def get_skills():
    return json.dumps(skills, default = lambda o: o.__dict__, sort_keys = True)

@app.route("/projects/<name>")
def projects(name = None):
    return render_template(f"projects.html", project_title = name)

@app.errorhandler(404)
def handle_404(error):
    return "Page Not Found"

os.system("cls")
workingdir = os.path.abspath(os.getcwd())
skills = read_skills()
app.run(host = "0.0.0.0", port = 8080, debug = True)
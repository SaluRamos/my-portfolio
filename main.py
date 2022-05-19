from flask import Flask, render_template, send_from_directory, redirect, url_for
import os
import json

app = Flask(__name__, static_url_path = "", static_folder = "static", template_folder = "templates")

class Skill():

    def __init__(self, name, rate = "✍🏻"):
        self.name = name
        self.rate = rate

class Project():

    def __init__(self, name, description, status, status_color, technologies):
        self.name = name
        self.description = description
        self.status = status
        self.status_color = status_color
        self.technologies = technologies
        # status pode ser: versão estável (funcinonal), legado (antigo, desatualizado ou não funciona), não terminado (não funcional ou falta de ferramentas), em progresso (foco atual)

def read_skills():
    skills = []
    with open("skills.txt", "r", encoding = "utf-8") as f:
        for i in f.readlines():
            name = i.split(";")[0]
            try:
                float(i.split(";")[1])
                rate = f"{i.split(';')[1]} of 5 ⭐"
                skills.append(Skill(name, rate))
            except:
                rate = f"{i.split(';')[1]}"
                skills.append(Skill(name, rate))
    return skills

def read_projects():
    projects = []
    with open("projects.txt", "r", encoding = "utf-8") as f:
        for i in f.readlines():
            name = i.split(";")[0].upper()
            description = f"{i.split(';')[1]}..."
            status = i.split(";")[2]
            status_color = i.split(";")[3]
            technologies = i.split(";")[4].split(",")
            projects.append(Project(name, description, status, status_color, technologies))
    return projects

def object_to_json(self):
    return json.dumps(self, default = lambda o: o.__dict__)

@app.route("/")
def index():
    return render_template("index.html", skills = skills, projects = projects)

@app.route("/curriculum_vitae")
def curriculum_vitae():
    return send_from_directory(f"{workingdir}/static/pdf/", "curriculum_vitae.pdf")

@app.route("/skills", methods = ['GET',])
def get_skills():
    return object_to_json(skills)

@app.route("/projects/<name>")
def projects(name = None):
    return render_template(f"projects.html", project_title = name)

@app.errorhandler(404)
def handle_404(error):
    return "Page Not Found"

os.system("cls")
workingdir = os.path.abspath(os.getcwd())
skills = read_skills()
projects = read_projects()
app.run(host = "0.0.0.0", port = 8080, debug = True)
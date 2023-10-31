from flask import Flask, render_template, request, flash, redirect, get_flashed_messages, session, send_from_directory, send_file
from flask_session import Session
import pandas as pd
import os
from werkzeug.utils import secure_filename
import Bigbrain
from openpyxl import Workbook
from waitress import serve
import glob
from zipfile import ZipFile


UPLOAD_FOLDER = r'Website Backend Code\uploads'
DOWNLOAD_FOLDER = r'Website Backend Code\downloads'
ALLOWED_EXTENSIONS = {'zip'}
app = Flask(__name__)
app.secret_key = '12345'
app.config['UPLOAD_FOLDER'], app.config['DOWNLOAD_FOLDER'] = UPLOAD_FOLDER, DOWNLOAD_FOLDER
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
options = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F", "Table of Summary", "Teams Travel Time"]
teams = ["Team A", "Team B", "Team C", "Team D", "Team E", "Team F"]
teamsdfs = {}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def initialpage():
    get_flashed_messages()
    if request.method == 'POST':
        yesorno = request.form.get('useourtraveltime')
        if 'zipfile' not in request.files:
            flash('No file part! Please try again')
            return redirect(request.url)
        file = request.files['zipfile']
        if file.filename == '':
            flash('No selected file! Please try again')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return render_template('success.html', done=False, yn=yesorno, file_path=file_path)
        flash('Invalid file! Please try again')
        return redirect(request.url)
    return render_template('index.html')

@app.route('/processing_data', methods=['GET', 'POST'])  
def index2():
    get_flashed_messages()
    if request.method == 'POST':
        file_path = request.form.get("file_path")
        yesorno = request.form.get("yn")
        listofdfs = Bigbrain.getrosters(os.path.join(app.root_path, r'uploads'), yesorno)
        for count in range(len(options)):
            teamsdfs[options[count]] = listofdfs[count]
        session['dfsdict'] = teamsdfs
        os.remove(file_path)
        files = glob.glob(os.path.join(app.root_path, r'downloads\*'))
        for f in files:
            os.remove(f)
        for teamid in options:
            file = teamsdfs[teamid]
            if teamid in teams:
                filename = "Patrol Plan for {}.xlsx".format(teamid)
            else:
                filename = "{}.xlsx".format(teamid)
            file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
            new_excel = pd.ExcelWriter(file_path)
            file.to_excel(new_excel, index=False)
            new_excel.close()
        return render_template('success.html', done=True)

@app.route('/view_results', methods=['GET', 'POST'])  
def results():
    return render_template('index2.html', teams=teams, options=options, csv=None)

@app.route('/show_data', methods=['GET', 'POST'])
def showData():
    teamsdfs = session.get("dfsdict")
    team = request.form.get("team")
    if team == None:
        return render_template('index2.html', teams=teams, options=options, csv=None)
    teamdf = teamsdfs[team]
    csv = teamdf.to_html()
    return render_template('index2.html', teams=teams, csv=csv, teamname=team, options=options)

@app.route('/download_all', methods=['GET', 'POST'])
def downloadData():
    download = request.form.get("download option")
    dir_path = os.path.join(app.root_path, r'downloads')
    os.chdir(dir_path)
    if download == "Download ALL Patrol Plans Excel files":
        filename = "Patrol Plans Excel Files.zip"
        with ZipFile(filename, "w") as newzip:
            for teamid in teams:
                newzip.write("Patrol Plan for {}.xlsx".format(teamid))
        os.chdir(os.path.dirname(app.root_path))
        return send_file(os.path.join(app.root_path, "downloads", filename), as_attachment=True)
    elif download == "Download ALL Patrol Plans, Table of Summary and Travel Times Excel files":
        filename = "Patrol Plans, Table of Summary and Teams Travel Times Excel Files.zip"
        with ZipFile(filename, "w") as newzip:
            for option in options:
                if option in teams:
                    newzip.write("Patrol Plan for {}.xlsx".format(option))
                else:
                    newzip.write("{}.xlsx".format(option))
        os.chdir(os.path.dirname(app.root_path))
        return send_file(os.path.join(app.root_path, "downloads", filename), as_attachment=True)
    return download

@app.route('/download/<filename>', methods=['GET', 'POST'])
def openexcel(filename):
    dir_path = os.path.join(app.root_path, r'downloads')
    return send_from_directory(dir_path, filename, as_attachment=True)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
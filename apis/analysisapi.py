import shutil
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash, g, Blueprint,abort

from database import User,Adcode,Scenecode,ScrapeMissions,db,CommonParameters_tagged,DBSession

from decorators import login_required
import os
from toolbox import downloadcsvanalysis,allowed_file,upload_file
from config import UPLOAD_FOLDER,DIRECTORY
from werkzeug.utils import secure_filename


analysis = Blueprint('analysis', __name__)


@analysis.route('/analysis/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        return render_template('analysis.html')


@analysis.route('/analysis/new_mission', methods=['GET', 'POST'])
def new_mission():
    if request.method == 'GET':
        return render_template('analysis_new_mission.html')

@analysis.route('/analysis/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('analysis.new_mission'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('analysis.new_mission'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(DIRECTORY, filename))
            upload_file(filename)
            return redirect(url_for('analysis.new_mission',
                                    filename=filename))

    return render_template('analysis_new_mission.html')



@analysis.route('/analysis/data_search', methods=['GET','POST'])
def data_search():
    if request.method == 'GET':
        return render_template('analysis_data_search.html')
    else:
        _city = request.form.get('city')
        city = _city[0:-1]
        commonparameters_tagged = CommonParameters_tagged.query.filter(CommonParameters_tagged.city == city).limit(1000).all()
        downloadcsvanalysis(city)

        return render_template('analysis_data_search.html', commonparameters_tagged=commonparameters_tagged)

@analysis.route('/analysis/data_search/download/', methods=['GET'])
def download2():
    filename = "downloadcsvanalysis.xls"
    return send_from_directory(DIRECTORY, filename, as_attachment=True)


import shutil
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash, g, Blueprint
from config import HOST,DB,PASSWD,PORT,USER,ADSL_SERVER_AUTH,ADSL_SERVER_URL,KEYS,TABLE_NAME
import config
from database import User,Adcode,Scenecode,ScrapeMissions,db

from decorators import login_required
import json
import pymysql
import xlwt
import os
import time


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


@analysis.route('/analysis/data_search', methods=['GET', 'POST'])
def data_search():
    if request.method == 'GET':
        return render_template('analysis_data_search.html')
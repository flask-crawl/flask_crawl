from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, EqualTo
import pymysql
from config import HOST,USER,PASSWD,DB,TABLE_NAME_INDEX,TABLE_NAME_ANALYSIS,ALLOWED_EXTENSIONS,DIRECTORY
import xlwt
from database import Adcode
import os
import xlrd

def downloadcsvindex(city,scene):
    conn = pymysql.connect(host=HOST, user=USER, password=PASSWD, db=DB, charset='utf8')
    cur = conn.cursor()
    sql = """
            select * from {} where city_adcode='{}' and typecode like '{}%'
            """.format(TABLE_NAME_INDEX,city,remove_zero(scene))
    cur.execute(sql)
    total_res = cur.fetchall()
    fields = cur.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('table_message', cell_overwrite_ok=True)

    # 写上字段信息
    for field in range(0, len(fields)):
        sheet.write(0, field, fields[field][0])

    # 获取并写入数据段信息

    for row in range(1, len(total_res) + 1):
        for col in range(0, len(fields)):
            sheet.write(row, col, u'%s' % total_res[row - 1][col])

    workbook.save(r'./downlaodcsvindex.xls')
    conn.close()

def downloadcsvanalysis(city):
    conn = pymysql.connect(host=HOST, user=USER, password=PASSWD, db=DB, charset='utf8')
    cur = conn.cursor()
    sql = """
            select * from {} where city='{}'
            """.format(TABLE_NAME_ANALYSIS,city)
    cur.execute(sql)
    total_res = cur.fetchall()
    fields = cur.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('table_message', cell_overwrite_ok=True)

    # 写上字段信息
    for field in range(0, len(fields)):
        sheet.write(0, field, fields[field][0])

    # 获取并写入数据段信息

    for row in range(1, len(total_res) + 1):
        for col in range(0, len(fields)):
            sheet.write(row, col, u'%s' % total_res[row - 1][col])

    workbook.save(r'./downloadcsvanalysis.xls')
    conn.close()

def remove_zero(input):
    b = str(input)[::-1]
    b = str(int(b))
    output = b[::-1]

    return output

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def upload_file(filename):

    book = xlrd.open_workbook(str(os.path.join(DIRECTORY, filename)))
    sheet = book.sheets()[0]

    conn = pymysql.connect(host=HOST, user=USER, password=PASSWD, db=DB, charset='utf8')

    cursor = conn.cursor()
    query = """INSERT INTO commonparameters_tagged (dt,province,city,region,cgi,tac,chinesename,covertype,scenario,vendor,earfcn,nettype,pci,iscore,gpslat,gpslng,bdlat,bdlng,angle,height,totaltilt,iscounty,isauto,flag,residential_flag,hospital_flag,beauty_spot_flag,college_flag,food_centre_flag,subway_flag,high_speed_flag,high_speed_rail_flag,viaduct_flag,high_rise_flag)
       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    for r in range(1, sheet.nrows):
        dt = sheet.cell(r, 0).value
        province = sheet.cell(r, 1).value
        city = sheet.cell(r, 2).value
        region = sheet.cell(r,3).value
        cgi = sheet.cell(r, 4).value
        tac = int(sheet.cell(r, 5).value)
        chinesename = sheet.cell(r, 6).value
        covertype = sheet.cell(r, 7).value
        scenario = sheet.cell(r, 8).value
        vendor = sheet.cell(r, 9).value
        earfcn = int(sheet.cell(r, 10).value)
        nettype = sheet.cell(r, 11).value
        pci = int(sheet.cell(r, 12).value)
        iscore = sheet.cell(r, 13).value
        gpslat = float(sheet.cell(r, 14).value)
        gpslng = float(sheet.cell(r, 15).value)
        bdlat = float(sheet.cell(r, 16).value)
        bdlng = float(sheet.cell(r, 17).value)
        angle = int(sheet.cell(r, 18).value)
        height = sheet.cell(r, 19).value
        totaltilt = float(sheet.cell(r, 20).value)
        iscounty = bool(sheet.cell(r, 21).value)
        isauto = bool(sheet.cell(r, 22).value)
        flag = bool(sheet.cell(r, 23).value)
        residential_flag = 0
        hospital_flag = 0
        beauty_spot_flag = 0
        college_flag = 0
        food_centre_flag = 0
        subway_flag = 0
        high_speed_flag = 0
        high_speed_rail_flag = 0
        viaduct_flag = 0
        high_rise_flag = 0

        values = (dt,province,city,region,cgi,tac,chinesename,covertype,scenario,vendor,earfcn,nettype,pci,iscore,gpslat,gpslng,bdlat,bdlng,angle,height,totaltilt,iscounty,isauto,flag,residential_flag,hospital_flag,beauty_spot_flag,college_flag,food_centre_flag,subway_flag,high_speed_flag,high_speed_rail_flag,viaduct_flag,high_rise_flag)
        cursor.execute(query, values)
    cursor.close()
    conn.commit()
    conn.close()

class RegisterForm(FlaskForm):
    username = StringField(u'用户名', validators=[DataRequired()])

    password = PasswordField(u'密码', validators=[DataRequired()])

    password2 = PasswordField(u'确认密码', validators=[DataRequired(), EqualTo('password', '两次密码不一致')])

    email = StringField(u'工作邮箱', validators=[DataRequired()], )

    submit = SubmitField(u'立即注册')


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])

    password = PasswordField(validators=[DataRequired()])

    submit = SubmitField(u'登录')


class CardForm(FlaskForm):
    title = StringField(validators=[DataRequired()])

    content = TextAreaField(validators=[DataRequired()])

    submit = SubmitField(u'立即发布')


class CommentForm(FlaskForm):
    content = StringField(validators=[DataRequired()])

    # title = StringField(validators=[DataRequired()])
    #
    # content = StringField(validators=[DataRequired()])

    submit = SubmitField(u'发表评论')


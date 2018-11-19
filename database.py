# conding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy, model
from datetime import datetime
from config import SQLALCHEMY_DATABASE_URI
from werkzeug.security import check_password_hash, generate_password_hash


db = SQLAlchemy()

engine = create_engine(SQLALCHEMY_DATABASE_URI)
DBSession = sessionmaker(bind=engine)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(50), unique=True)

    username = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(256))

    is_activate = db.Column(db.Boolean, default=False)

    is_delete = db.Column(db.Boolean, default=False)

    def model_to_dict(self):
        return {"id":self.id, "name":self.u_name, "email":self.u_email, "password":self.u_password}

    #flask自带加密编码
    def set_password(self, password):
        self.u_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.u_password, password)

    def check_permission(self, permission):
        return self.u_permission & permission == permission


#帖子
class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(64), nullable=False)

    content = db.Column(db.Text, nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now, index=True)

    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))


    author = db.relationship('User', backref=db.backref('notes'))


#评论
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    content = db.Column(db.Text, nullable=False)

    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    create_time = db.Column(db.DateTime, default=datetime.now, index=True)


    note = db.relationship('Note', backref=db.backref('comments', order_by = id.desc()))

    author = db.relationship('User', backref=db.backref('comments'))



class Adcode(db.Model):
    __tablename__ = 'adcode'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    province = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    adcode = db.Column(db.Integer, nullable=False)


class Scenecode(db.Model):
    __tablename__ = 'scenecode'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    scene = db.Column(db.String(50), nullable=False)
    scenecode = db.Column(db.String(50), nullable=False)



class ScrapeMissions(db.Model):
    __tablename__ = 'scrape_missions'

    id = db.Column(db.Integer, autoincrement=True)

    username = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(50), nullable=False)

    city = db.Column(db.String(50), nullable=False)

    city_adcode = db.Column(db.String(6), primary_key=True)

    scene = db.Column(db.String(50), nullable=False)

    type_code = db.Column(db.String(6), primary_key=True)

    resolution = db.Column(db.Float, default=0.02)

    status = db.Column(db.String(100), nullable=False)

    final_grid = db.Column(db.Integer, default=0)

    adsl_server_url = db.Column(db.String(100), nullable=False)

    adsl_auth = db.Column(db.String(100), nullable=False)

    keys = db.Column(db.Text, nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)


class GaodeMapScene(db.Model):
    __tablename__ = 'gaodemapscene'

    id = db.Column(db.String(20),primary_key=True)

    province = db.Column(db.String(50))

    city = db.Column(db.String(50))

    name = db.Column(db.String(50))

    city_adcode = db.Column(db.String(20))

    district = db.Column(db.String(50))

    address = db.Column(db.String(100))

    longtitude = db.Column(db.Float(scale=10))

    lat = db.Column(db.Float(scale=10))

    type = db.Column(db.String(100))

    typecode = db.Column(db.String(20))

    classify = db.Column(db.String(100))

    area = db.Column(db.Float(scale=10))

    shape = db.Column(db.Text)

    wgs_long = db.Column(db.Float(scale=10))

    wgs_lat = db.Column(db.Float(scale=10))

    wgs_shape = db.Column(db.Text)


class CommonParameters(db.Model):
    __tablename__ = 'commonparameters'
    dt = db.Column(db.String(50))
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    region = db.Column(db.String(50))
    cgi = db.Column(db.String(50), primary_key=True)
    tac = db.Column(db.Integer, default=0)
    chinesename = db.Column(db.String(200))
    covertype = db.Column(db.String(50))
    scenario = db.Column(db.String(50))
    vendor = db.Column(db.String(50))
    earfcn = db.Column(db.Integer, default=0)
    nettype = db.Column(db.String(50))
    pci = db.Column(db.Integer, default=0)
    iscore = db.Column(db.Boolean, default=False)
    gpslat = db.Column(db.Float(scale=10))
    gpslng = db.Column(db.Float(scale=10))
    bdlat = db.Column(db.Float(scale=10))
    bdlng = db.Column(db.Float(scale=10))
    angle = db.Column(db.Integer, default=0)
    height = db.Column(db.String(50))
    totaltilt = db.Column(db.Float(scale=10))
    iscounty  = db.Column(db.Boolean, default=False)
    isauto = db.Column(db.Boolean, default=False)
    flag = db.Column(db.Boolean, default=False)
    # residential_flag = db.Column(db.Boolean, default=False)
    # hospital_flag = db.Column(db.Boolean, default=False)
    # beauty_spot_flag = db.Column(db.Boolean, default=False)
    # college_flag = db.Column(db.Boolean, default=False)
    # food_centre_flag = db.Column(db.Boolean, default=False)
    # subway_flag = db.Column(db.Boolean, default=False)
    # high_speed_flag = db.Column(db.Boolean, default=False)
    # high_speed_rail_flag = db.Column(db.Boolean, default=False)
    # viaduct_flag = db.Column(db.Boolean, default=False)
    # high_rise_flag = db.Column(db.Boolean, default=False)

class CommonParameters_tagged(db.Model):
    __tablename__ = 'commonparameters_tagged'
    dt = db.Column(db.String(50))
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    region = db.Column(db.String(50))
    cgi = db.Column(db.String(50), primary_key=True)
    tac = db.Column(db.Integer, default=0)
    chinesename = db.Column(db.String(200))
    covertype = db.Column(db.String(50))
    scenario = db.Column(db.String(50))
    vendor = db.Column(db.String(50))
    earfcn = db.Column(db.Integer, default=0)
    nettype = db.Column(db.String(50))
    pci = db.Column(db.Integer, default=0)
    iscore = db.Column(db.Boolean, default=False)
    gpslat = db.Column(db.Float(scale=10))
    gpslng = db.Column(db.Float(scale=10))
    bdlat = db.Column(db.Float(scale=10))
    bdlng = db.Column(db.Float(scale=10))
    angle = db.Column(db.Integer, default=0)
    height = db.Column(db.String(50))
    totaltilt = db.Column(db.Float(scale=10))
    iscounty  = db.Column(db.Boolean, default=False)
    isauto = db.Column(db.Boolean, default=False)
    flag = db.Column(db.Boolean, default=False)
    residential_flag = db.Column(db.String(50), default=False)
    hospital_flag = db.Column(db.String(50), default=False)
    beauty_spot_flag = db.Column(db.String(50), default=False)
    college_flag = db.Column(db.String(50), default=False)
    food_centre_flag = db.Column(db.String(50), default=False)
    subway_flag = db.Column(db.String(50), default=False)
    high_speed_flag = db.Column(db.String(50), default=False)
    high_speed_rail_flag = db.Column(db.String(50), default=False)
    viaduct_flag = db.Column(db.String(50), default=False)
    high_rise_flag = db.Column(db.String(50), default=False)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, EqualTo



def remove_zero(input):
    b = str(input)[::-1]
    b = str(int(b))
    output = b[::-1]

    return output


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


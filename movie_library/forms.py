from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
    URLField,
)

from wtforms.validators import (
    InputRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
)


class LoginForm(FlaskForm):
    email = StringField("電子郵件", validators=[InputRequired(), Email()])
    password = PasswordField("密碼", validators=[InputRequired()])
    submit = SubmitField("登入")


class RegisterForm(FlaskForm):
    email = StringField("電子郵件", validators=[InputRequired(), Email()])

    password = PasswordField(
        "密碼",
        validators=[
            InputRequired(),
            Length(
                min=4,
                max=20,
                message="密碼需大於4個數字.",
            ),
        ],
    )

    confirm_password = PasswordField(
        "確認密碼",
        validators=[
            InputRequired(),
            EqualTo(
                "password",
                message="密碼輸入錯誤",
            ),
        ],
    )

    submit = SubmitField("註冊")


class MovieForm(FlaskForm):
    title = StringField("標題", validators=[InputRequired()])
    director = StringField("導演", validators=[InputRequired()])

    year = IntegerField(
        "發行年分",
        validators=[
            InputRequired(),
            NumberRange(min=1878, message="請輸入正確年分"),
        ],
    )

    submit = SubmitField("添加新電影")


class StringListField(TextAreaField):
    def _value(self):
        if self.data:
            return "\n".join(self.data)
        else:
            return ""

    def process_formdata(self, valuelist):
        # checks valuelist contains at least 1 element, and the first element isn't falsy (i.e. empty string)
        if valuelist and valuelist[0]:
            self.data = [line.strip() for line in valuelist[0].split("\n")]
        else:
            self.data = []


class ExtendedMovieForm(MovieForm):
    cast = StringListField("演員")
    series = StringListField("系列")
    tags = StringListField("標籤")
    description = TextAreaField("電影介紹")
    video_link = URLField("連結")

    submit = SubmitField("提交")

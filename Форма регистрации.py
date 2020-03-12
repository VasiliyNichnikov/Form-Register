from flask import Flask
from flask import render_template, request
from data.user import User
from data import db_session
from Форма import RegisterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['GET', 'POST'])
def main():
    form = RegisterForm()
    if request.method == 'POST':
        user = User()
        user.email = request.form['login_email']
        user.hashed_password = request.form['password']
        user.surname = request.form['surname']
        user.name = request.form['name']
        user.age = request.form['age']
        user.position = request.form['position']
        user.speciality = request.form['specialty']
        user.address = request.form['address']
        session = db_session.create_session()
        session.add(user)
        session.commit()
        return 'Пользователь добавлен в базу данных.'
    return render_template('register.html', title='Форма регистрации', form=form)


if __name__ == "__main__":
    db_session.global_init("db/users.sqlite")
    app.run()
from data import db_session
from data.users import User
from data.news import News
import datetime

db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

user = User()
user.name = "Пользователь 1"
user.about = "Новость пользователя 1"
user.email = "email1@email.ru"
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Пользователь 2"
user.about = "Новость пользователя 2"
user.email = "email2@email.ru"
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Пользователь 3"
user.about = "Новость пользователя 3"
user.email = "email3@email.ru"
db_sess.add(user)
db_sess.commit()

news = News(title="Первая новость", content="Привет блог!",
            user_id=1, is_private=False)
db_sess.add(news)
db_sess.commit()

user = db_sess.query(User).filter(User.id == 1).first()
news = News(title="Вторая новость", content="Уже вторая запись!",
            user=user, is_private=False)
db_sess.add(news)
db_sess.commit()

user = db_sess.query(User).filter(User.id == 1).first()
news = News(title="Личная запись", content="Эта запись личная",
            is_private=True)
user.news.append(news)
db_sess.commit()
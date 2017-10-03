from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    user_img = db.Column(db.String)

    def __init__(self, username, password, name, email, user_img):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.user_img = user_img

    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    code = db.Column(db.Text)
    content = db.Column(db.Text)
    post_img = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, title, code, content, post_img, user_id):
        self.title = title
        self.code = code
        self.content = content
        self.post_img = post_img
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.title


class Comments(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comment = db.Column(db.Text)

    post = db.relationship('Post', foreign_keys=post_id)

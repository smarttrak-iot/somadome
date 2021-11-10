from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    displayname = db.Column(db.String(80), nullable=True)
    headline = db.Column(db.String(80), nullable=True)
    firstName = db.Column(db.String(80), nullable=True)
    middleInitial = db.Column(db.String(80), nullable=True)
    lastName = db.Column(db.String(80), nullable=True)
    suffix = db.Column(db.String(80), nullable=True)
    phone = db.Column(db.String(80), nullable=True)
    address1 = db.Column(db.String(80), nullable=True)
    address2 = db.Column(db.String(80), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    state = db.Column(db.String(80), nullable=True)
    zip = db.Column(db.String(80), nullable=True)
    joinDate = db.Column(db.Date, nullable=True)
    birthDate = db.Column(db.Date, nullable=True)



    @classmethod
    def find_by_username(cls, username: str) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email: str) -> "UserModel":
        return cls.query.filter_by(email=email).first()  

    @classmethod
    def find_by_id(cls, _id: int) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
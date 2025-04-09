from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from datetime import datetime

db = SQLAlchemy()

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'
    id_user: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    biography: Mapped[str] = mapped_column(String(120), nullable=True)
    creat_date: Mapped[datetime] = mapped_column(Date, nullable=False)

class Publications(Base): 
    __tablename__ = 'publicaciones'
    id_publication: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id_user'))
    publication: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(String(120), nullable=True)
    publication_date: Mapped[datetime] = mapped_column(Date, nullable=False)

class Comments(Base): 
    __tablename__ = 'comentarios'
    id_comment: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_publication: Mapped[int] = mapped_column(Integer, ForeignKey('publicaciones.id_publication'))
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id_user'))
    comment: Mapped[str] = mapped_column(String(120), nullable=False)
    comment_date: Mapped[datetime] = mapped_column(Date, nullable=False)

class Likes(Base): 
    __tablename__ = 'me_gusta'
    id_like: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_publication: Mapped[int] = mapped_column(Integer, ForeignKey('publicaciones.id_publication'))
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id_user'))
    like_date: Mapped[datetime] = mapped_column(Date, nullable=False)

class Followers(Base): 
    __tablename__ = 'seguidores'
    id_follower: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_user: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id_user'))
    id_followed: Mapped[int] = mapped_column(Integer, ForeignKey('usuarios.id_user'))
    follow_date: Mapped[datetime] = mapped_column(Date, nullable=False)

# Método para serializar información sensible
def serialize_user(self):
    return {
        "id_user": self.id_user,
        "email": self.email,
        # No serializamos contraseñas por motivos de seguridad
    }

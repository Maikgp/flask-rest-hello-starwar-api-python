from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritos = db.relationship('Favoritos', backref='user', lazy=True)
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id_user": self.id_user,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Personajes(db.Model):
    __tablename__ = 'Personajes'

    id_personajes = db.Column(db.Integer, primary_key=True)
    name_personajes = db.Column(db.String(120), unique=True, nullable=False)
    age_personajes = db.Column(db.String(80), unique=False, nullable=False)
    weapon_personajes = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritos = db.relationship('Favoritos', backref='Personajes', lazy=True)


    def __repr__(self):
        return '<Personajes %r>' % self.username

    def serialize(self):
        return {
            "id_personajes": self.id_personajes,
            "name_personajes": self.name_personajes,
            "age_personajes": self.age_personajes,
            "weapon_personajes": self.weapon_personajes,
            
        } 


    
class Planetas(db.Model):
    __tablename__ = 'Planetas'

    id_planeta = db.Column(db.Integer, primary_key=True)
    name_planeta = db.Column(db.String(120), unique=True, nullable=False)
    galaxia_planeta = db.Column(db.String(80), unique=False, nullable=False)
    size_planeta = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritos = db.relationship('Favoritos', backref='Planetas', lazy=True)


    def __repr__(self):
        return '<Planetas %r>' % self.username

    def serialize(self):
        return {
            "id_planeta": self.id_planeta,
            "name_planeta": self.name_planeta,
            "galaxia_planeta": self.Galaxia_planeta,
            "size_planeta": self.size_planeta,
            
        }
    
class Favoritos(db.Model):
    __tablename__ = 'Favoritos'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("user.id_user"))
    id_personajes = db.Column(db.Integer,db.ForeignKey("Personajes.id_personajes"))
    id_planeta = db.Column(db.Integer,db.ForeignKey("Planetas.id_planeta"))


    def __repr__(self):
        return '<Favoritos %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_personajes": self.id_personajes,
            "id_planeta": self.id_planeta,
            
        }           






from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritos_personajes = db.relationship('PersonajesFavoritos', backref='Usuarios', lazy=True)
    favoritos_personajes = db.relationship('PlanetasFavoritos', backref='Usuarios', lazy=True)




    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Personajes(db.Model):
    __tablename__ = 'Personajes'

    id_personaje = db.Column(db.Integer, primary_key=True)
    name_personaje = db.Column(db.String(120), unique=True, nullable=False)
    age_personaje = db.Column(db.String(80), unique=False, nullable=False)
    weapon_personaje = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritos_personajes = db.relationship('PersonajesFavoritos', backref='Personaje', lazy=True)


    def __repr__(self):
        return '<Personajes %r>' % self.username

    def serialize(self):
        return {
            "id_personaje": self.id_personaje,
            "name_personaje": self.name_personaje,
            "age_personaje": self.age_personaje,
            "weapon_personaje": self.weapon_personaje,
            
        } 

class PersonajesFavoritos(db.Model):
    __tablename__ = 'PersonajesFavoritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    personaje_id = db.Column(db.Integer,db.ForeignKey("personajes.id"))


    def __repr__(self):
        return '<PersonajesFavoritos %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personajes_id": self.personaje_id,
            
        }           
    
class Planetas(db.Model):
    __tablename__ = 'Planetas'

    id_planeta = db.Column(db.Integer, primary_key=True)
    name_planeta = db.Column(db.String(120), unique=True, nullable=False)
    Galaxia_planeta = db.Column(db.String(80), unique=False, nullable=False)
    size_planeta = db.Column(db.Boolean(), unique=False, nullable=False)


    def __repr__(self):
        return '<Planeta %r>' % self.username

    def serialize(self):
        return {
            "id_planeta": self.id_planeta,
            "name_planeta": self.name_planeta,
            "galaxia_planeta": self.Galaxia_planeta,
            "size_planeta": self.size_planeta,
            
        }
    
class PlanetasFavoritos(db.Model):
    __tablename__ = 'PlanetasFavoritos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    planeta_id = db.Column(db.Integer,db.ForeignKey("planeta.id"))


    def __repr__(self):
        return '<PlanetasFavoritos %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planeta_id": self.personaje_id,
            
        }    





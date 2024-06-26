"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planetas, Personajes, Favoritos
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/wipeall', methods=['GET'])
def database_wipe():
    try:
        db.reflect()
        db.drop_all()
        db.session.commit()
    except Exception as e:
        return "mec", 500
    return "ok", 200


@app.route('/')
def sitemap():
    return generate_sitemap(app)


#USERS

@app.route('/users', methods=['GET'])
def get_users():

    users = User.query.all()

    response_body = [user.serialize() for user in users]

    return jsonify(response_body), 200

@app.route('/user/<int:id_user>', methods=['GET'])
def get_user_profile(id_user):
    user = User.query.get(id_user)

    if user:
        return jsonify(user.serialize()), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    


#PERSONAJES

@app.route('/people', methods=['GET'])
def get_personajes():

    people = Personajes.query.all()

    response_body = [item.serialize() for item in people]

    return jsonify(response_body), 200


@app.route('/people/<int:id_personajes>', methods=['GET'])
def get_personaje(id_personajes):
    people = Personajes.query.get(id_personajes)

    if people:
        return jsonify(people.serialize()), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404


@app.route('/favorite/people/<int:people_id>', methods=['POST'])  
def agregar_people_favorito(id_personajes):
    
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    
    personaje = Personajes.query.get(id_personajes)
    if personaje is None:
        return jsonify({'error': 'Personaje no encontrado'}), 404

    favorito = Favoritos(id_user=user.id, id_personjes=id_people)
    db.session.add(favorito)
    db.session.commit()

    return jsonify({'message': f'Personaje {people.name} agregado a favoritos del usuario {user.name}'}), 200 




@app.route('/people/<int:id>', methods=['DELETE'])
def handle_delete_people(id):
    new_people = Personajes.query.get(id)
    db.session.delete(new_people)
    db.session.commit()

    for favorite in new_people.favorites:
        db.session.delete(favorite)

    response_body = {
       "msg":"personaje eliminado"
    }
    return jsonify(response_body), 200

    

#PLANETS

@app.route('/planets', methods=['GET'])
def get_planets():

    planets = Planetas.query.all()

    response_body = [item.serialize() for item in planets]

    return jsonify(response_body), 200


@app.route('/planet/<int:id_planeta>', methods=['GET'])
def get_planeta(id_planeta):
    planeta = Planetas.query.get(id_planeta)

    if planeta:
        return jsonify(planeta.serialize()), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404  
    

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])  #revisar que aqui hay que hacer el favorite planet planet id
def agregar_planeta_favorito(planet_id):
    
    user = User.query.get(id_user)
    if user is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    
    planeta = Planetas.query.get(planet_id)
    if planeta is None:
        return jsonify({'error': 'Planeta no encontrado'}), 404

    favorito = Favoritos(id_user=user.id, planeta_id=planeta.id)
    db.session.add(favorito)
    db.session.commit()

    return jsonify({'message': f'Planeta {planeta.name} agregado a favoritos del usuario {user.name}'}), 200   

@app.route('/planets/<int:id>', methods=['DELETE'])
def handle_delete_planet(id):
    new_planet = Planetas.query.get(id)
    db.session.delete(new_planet)
    db.session.commit()

    for favorite in new_planet.favorites:
        db.session.delete(favorite)

    response_body = {
       "msg":"planeta eliminado"
    }
    return jsonify(response_body), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)





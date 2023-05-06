import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Movie, Actor
import dateutil.parser
import datetime
from babel.dates import format_date, format_datetime, format_time
import dateutil.utils
from auth import requires_auth, AuthError


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/example
    if test_config is None:
        app.config.from_object('config-prod')
    else:
        app.config.from_object('config-test')

    #db = SQLAlchemy(app)
    db.init_app(app)
    # migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    CORS(app, resources={r"*": {"origins": '*'}})

    # CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Headers", "GET, POST, DELETE"
        )
        return response

    @app.route('/')
    def index():
        return "Hello Python"

    def format_dt(value, format='medium'):
        try:
            date = dateutil.parser.parse(value)
            if format == 'full':
                format = "EEEE MMMM, d, y 'at' h:mma"
            elif format == 'medium':
                format = "EE MM, dd, y h:mma"
            return format_datetime(date, format, locale='en')
        except Exception as e:
            abort(422, 'Date format is not correct')

    @app.route("/movie/<int:movie_id>", methods=["GET"])
    @requires_auth('read:movie')
    def get_movies(jwt, movie_id):
        movie = Movie.query.filter_by(id=movie_id).one_or_none()

        if movie is None:
            raise abort(404, "No Movie Found")

        return jsonify(
            {
                "success": True,
                "movie": movie.format(),
            }
        )

    @app.route("/movie", methods=["POST"])
    @requires_auth('add:movie')
    def save_movie(jwt):
        req = request.get_json()
        success = True
        movie_id = -1
        rel_date = format_dt(req['release_date'])
        try:
            movie = Movie(
                title=req['title'],
                release_date=rel_date
            )
            movie.insert()
            movie_id = movie.id
        except Exception as e:
            db.session.rollback()
            success = False
        finally:
            db.session.close()
        return jsonify(
            {
                "success": success,
                "movie_id": movie_id
            }
        )

    @app.route("/movie/<int:movie_id>", methods=["PATCH"])
    @requires_auth('edit:movie')
    def patch_movie(jwt, movie_id):
        success = True
        recordUpdated = 0

        movie = Movie.query.filter_by(id=movie_id).one_or_none()
        if movie is None:
            abort(404, 'No Movie Found')

        try:
            body = request.get_json()
            if 'title' in body:
                movie.title = body['title']

            if 'release_date' in body:
                movie.release_date = format_dt(body['release_date'])

            movie.update()
            recordUpdated = 1
        except Exception as e:
            db.session.rollback()
            success = False
        finally:
            db.session.close()
        return jsonify(
            {
                "success": success,
                "recordUpdated": recordUpdated
            }
        )

    @app.route("/movie/<int:movie_id>", methods=["DELETE"])
    @requires_auth('delete:movie')
    def delete_movie(jwt, movie_id):
        success = True
        recordDeleted = 0
        try:
            movie = Movie.query.filter_by(id=movie_id).one_or_none()
            if movie is not None:
                movie.delete()
                recordDeleted = 1
            else:
                success = False
        except Exception as e:
            db.session.rollback()
            success = False
        finally:
            db.session.close()
        return jsonify(
            {
                "success": success,
                "recordDeleted": recordDeleted
            }
        )

    @app.route("/actor/<int:actor_id>", methods=["GET"])
    @requires_auth('read:actor')
    def get_actor(jwt, actor_id):
        actor = Actor.query.filter_by(id=actor_id).one_or_none()

        if actor is None:
            raise abort(404, "No Actor Found")

        return jsonify(
            {
                "success": True,
                "actor": actor.format()
            }
        )

    @app.route("/actor", methods=["POST"])
    @requires_auth('add:actor')
    def save_actor(jwt):
        req = request.get_json()
        success = True
        actor_id = -1
        try:
            actor = Actor(
                name=req['name'],
                age=req['age'],
                gender=req['gender']
            )
            actor.insert()
            actor_id = actor.id
        except Exception as e:
            db.session.rollback()
            success = False
        finally:
            db.session.close()
        return jsonify(
            {
                "success": success,
                "actor_id": actor_id
            }
        )

    @app.route("/actor/<int:actor_id>", methods=["PATCH"])
    @requires_auth('edit:actor')
    def patch_actor(jwt, actor_id):
        success = True
        recordPatched = 0

        actor = Actor.query.filter_by(id=actor_id).one_or_none()
        if actor is None:
            raise abort(404, "No actor Found")
        try:
            body = request.get_json()
            if 'name' in body:
                actor.name = body['name']
            if 'age' in body:
                actor.age = body['age']
            if 'gender' in body:
                actor.gender = body['gender']

            actor.update()
            recordPatched = 1

        except Exception as e:
            db.session.rollback()
            success = False
        finally:
            db.session.close()
        return jsonify(
            {
                "success": success,
                "recordPatched": recordPatched
            }
        )

    @app.route("/actor/<int:actor_id>", methods=["DELETE"])
    @requires_auth('delete:actor')
    def delete_actor(jwt, actor_id):
        success = True
        recordDeleted = 0
        try:
            actor = Actor.query.filter_by(id=actor_id).one_or_none()
            if actor is not None:
                actor.delete()
                recordDeleted = 1
            else:
                raise abort(404, "No Actor Found")
        except Exception as e:
            db.session.rollback()
            success = False
        finally:
            db.session.close()
        return jsonify(
            {
                "success": success,
                "recordDeleted": recordDeleted
            }
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable",
            "description": error.description,
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error",
            "description": error.description,
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request",
            "description": error.description,
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found",
            "description": error.description
        }), 404

    @app.errorhandler(AuthError)
    def handle_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error,
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()

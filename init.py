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


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config-prod')
    else:
        app.config.from_object('config-test')

    #db = SQLAlchemy(app)
    db.init_app(app)
    migrate = Migrate(app, db)

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
        date = dateutil.parser.parse(value)
        if format == 'full':
            format = "EEEE MMMM, d, y 'at' h:mma"
        elif format == 'medium':
            format = "EE MM, dd, y h:mma"
        return format_datetime(date, format, locale='en')


    @app.route("/movies", methods=["GET"])
    def get_movies():
        all_movies = [movie.format() for movie in Movie.query.all()]

        return jsonify(
            {
                "success": True,
                "movies": all_movies,
            }
        )

    @app.route("/movie", methods=["POST"])
    def save_movie():
        req = request.get_json()
        success = True
        movie_id=-1
        try:
            movie = Movie(
                title=req['title'],
                release_date=format_dt(req['release_date'])
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

    @app.route("/movie/<int:movie_id>", methods=["DELETE"])
    def delete_movie(movie_id):
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

    @app.route("/actor", methods=["GET"])
    def get_actor():
        all_actors = [actor.format() for actor in Actor.query.all()]

        return jsonify(
            {
                "success": True,
                "actors": all_actors,
            }
        )

    @app.route("/actor", methods=["POST"])
    def save_actor():
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

    @app.route("/actor/<int:actor_id>", methods=["DELETE"])
    def delete_actor(actor_id):
        success = True
        recordDeleted = 0
        try:
            actor = Actor.query.filter_by(id=actor_id).one_or_none()
            if actor is not None:
                actor.delete()
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

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable",
            "description": error.description,
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found",
            "description": error.description
        }), 404

    # @app.errorhandler(AuthError)
    # def handle_error(error):
    #     return jsonify({
    #         "success": False,
    #         "error": error.status_code,
    #         "message": error.error,
    #     }), error.status_code

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run()

import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import setup_db, Person
import json


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello"
        # greeting = Person.catchphrase
        if excited == 'true' : greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/greeting', methods=['POST'])
    def create_greeting():
        body = request.get_json()

        new_name = body['name']
        new_catchphrase = body['catchphrase']

        try:
            new_person = Person(name=new_name, catchphrase=new_catchphrase)
            new_person.insert()

            return jsonify({
                'success': True,
                'created': new_person.name
            })

        except:
            abort(422)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
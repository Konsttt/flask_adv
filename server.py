from flask import Flask, jsonify, request
from flask.views import MethodView
from db import Session_maker
from model import Adv, User
from db import session_q
from schema import HttpError, CreateUser, validate
from sqlalchemy.exc import IntegrityError
from hashlib import md5

adv_app = Flask('adv_app')


@adv_app.errorhandler(HttpError)
def error_handler(error: HttpError):

    response = jsonify({'status': 'error', 'description': error.description})
    response.status_code = error.status_code
    return response


class UserView(MethodView):

    def post(self):
        json_data = request.json
        json_data = validate(json_data, CreateUser)
        json_data['password'] = md5(str(json_data['password']).encode()).hexdigest()
        with Session_maker() as session:
            user = User(**json_data)
            session.add(user)
            try:
                session.commit()
            except IntegrityError as er:
                raise HttpError(409, 'user already exists')
            return jsonify({'id': user.id})

    def delete(self, adv_users_id: int):
        with Session_maker() as session:
            user = get_adv(adv_users_id, session)
            session.delete(user)
            session.commit()
            return jsonify({'status': 'deleted'})

def get_adv(adv_id: int, session: Session_maker):
    adv = session.get(Adv, adv_id)
    if adv is None:
        raise HttpError(404, 'This advertisement not found')
    return adv


class AdvView(MethodView):

    def get(self, adv_id=None):
        if adv_id:
            with Session_maker() as session:
                adv = get_adv(adv_id, session)
                return jsonify({'id': adv.id, 'title': adv.title, 'message': adv.message,
                                'date': adv.creation_time.isoformat(), 'owner': adv.owner})
        else:
            all_adv = session_q.query(Adv).all()
            all_adv_list = []
            for adv in all_adv:
                all_adv_list.append({adv.id: {'title': adv.title, 'message': adv.message,
                                 'date': adv.creation_time.isoformat(), 'owner': adv.owner}})
            return all_adv_list

    def post(self):
        json_data = request.json
        with Session_maker() as session:
            adv = Adv(**json_data)
            session.add(adv)
            session.commit()
            return {'id': adv.id}

    def patch(self, adv_id: int):
        json_data = request.json
        with Session_maker() as session:
            adv = get_adv(adv_id, session)
            for field, value in json_data.items():
                setattr(adv, field, value)
            session.add(adv)
            session.commit()
            return jsonify({'status': 'patched'})

    def delete(self, adv_id: int):
        with Session_maker() as session:
            adv = get_adv(adv_id, session)
            session.delete(adv)
            session.commit()
            return jsonify({'status': 'deleted'})


adv_app.add_url_rule('/adv/<adv_id>/', view_func=AdvView.as_view('adv'), methods=['GET', 'PATCH', 'DELETE'])
adv_app.add_url_rule('/adv/', view_func=AdvView.as_view('adv_create'), methods=['POST', 'GET'])
adv_app.add_url_rule('/user/', view_func=UserView.as_view('user_create'), methods=['POST'])
adv_app.add_url_rule('/user/<adv_users_id>/', view_func=UserView.as_view('user_delete'), methods=['DELETE'])

if __name__ == '__main__':
    adv_app.run()

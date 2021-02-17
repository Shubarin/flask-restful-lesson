from flask import Flask
from flask_restful import Api

from data import db_session

from lesson_12_flask_restful import jobs_resources, users_resources

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    api.add_resource(jobs_resources.JobsListResource, '/api/jobs')
    api.add_resource(jobs_resources.JobsResource, '/api/jobs/<int:jobs_id>')
    api.add_resource(users_resources.UsersListResource, '/api/users')
    api.add_resource(users_resources.UserResource, '/api/users/<int:user_id>')
    app.run(host='localhost', port=5000)


if __name__ == '__main__':
    main()

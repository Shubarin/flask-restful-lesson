from requests import get, post, delete


def test_jobs_api():
    print(get('http://localhost:5000/api/jobs').json())

    print(get('http://localhost:5000/api/jobs/1').json())
    print(get('http://localhost:5000/api/jobs/999').json())

    # print(get('http://localhost:5000/api/jobs/q').json())

    # запрос без параметров
    print(post('http://localhost:5000/api/jobs').json())
    # # запрос с неверным количеством параметрами
    print(post('http://localhost:5000/api/jobs',
               json={'team_leader': 1}).json())
    print(post('http://localhost:5000/api/jobs',
               json={'id': 5,
                     'team_leader': 1,
                     'job': 'Текст работы',
                     'work_size': 1,
                     'category': 1,
                     'collaborators': '1, 2',
                     'is_finished': True}).json())

    print(delete('http://localhost:5000/api/jobs/999').json())
    # работы с id = 999 нет в базе

    print(delete('http://localhost:5000/api/jobs/2').json())

    print(get('http://localhost:5000/api/jobs').json())


def test_users_api():
    print(get('http://localhost:5000/api/users').json())

    print(get('http://localhost:5000/api/users/1').json())
    print(get('http://localhost:5000/api/users/999').json())

    # запрос без параметров
    print(post('http://localhost:5000/api/users').json())
    # запрос с неверным количеством параметрами
    print(post('http://localhost:5000/api/users',
               json={'id': 1}).json())
    print(post('http://localhost:5000/api/users',
               json={'id': 2,
                     'name': 'Test',
                     'surname': 'Testing',
                     'age': 42,
                     'position': 'position',
                     'speciality': 'speciality',
                     'address': 'Воронеж',
                     'email': 'b@b.com'}).json())

    print(delete('http://localhost:5000/api/users/999').json())
    # пользователя с id = 999 нет в базе

    print(delete('http://localhost:5000/api/users/1').json())

    print(get('http://localhost:5000/api/users').json())

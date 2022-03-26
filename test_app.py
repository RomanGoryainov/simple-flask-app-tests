from app import app

def test_main():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_hello():
    response = app.test_client().get('/howareyou')

    assert response.status_code == 200
    assert response.data == b'I am good, how about you?'
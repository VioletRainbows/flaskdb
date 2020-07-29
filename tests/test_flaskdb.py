from flaskdb.data_models import User


def test_insert_a(db_session):
    assert db_session.query(User.username).count() == 0
    db_session.add(User(username='unit-tests'))
    db_session.commit()
    assert db_session.query(User.username).count() == 1


def test_insert_b(db_session):
    assert db_session.query(User.username).count() == 0
    db_session.add(User(username='unit-tests'))
    db_session.commit()
    assert db_session.query(User.username).count() == 1

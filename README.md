# Installation/Tests
```
pip install -r requirements.txt
export DATABASE_URI=postgresql+psycopg2://[username]:[password]@localhost:5432/[database]
pytest
```

# Issue
Warnings should not be present.
```
$ pytest 
======================================= test session starts ========================================
platform linux -- Python 3.8.0, pytest-6.0.0, py-1.9.0, pluggy-0.13.1
rootdir: /home/mia/workspace/flaskdb, configfile: setup.cfg, testpaths: tests
plugins: mock-3.2.0, flask-sqlalchemy-1.0.2
collected 2 items                                                                                  

tests/test_flaskdb.py ..                                                                     [100%]

========================================= warnings summary =========================================
tests/test_flaskdb.py::test_insert_a
tests/test_flaskdb.py::test_insert_b
  /home/mia/.virtualenvs/flaskdb/lib/python3.8/site-packages/sqlalchemy/pool/base.py:884: SAWarning: Reset agent is not active.  This should not occur unless there was already a connectivity error in progress.
    util.warn(

-- Docs: https://docs.pytest.org/en/stable/warnings.html
```

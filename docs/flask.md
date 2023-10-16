## flask-migrate 建表
依次执行以下命令
```shell
$ export FLASK_APP=manage.py
# windows 系统：set FLASK_APP=manage.py

$ flask db init
$ flask db migrate
$ flask db upgrade
```
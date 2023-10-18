
## 结构

### job_web
python version: v3.8
vue: 3
bootstrap: 5.3.2

## TODO
- [ ] flask_login怎么用？
- [ ] bootstrap 如何与vue整合
- [ ] 增加一个表单提交示例
- [ ] python定时任务
- [ ] python爬虫
- [ ] flask生产配置应该如何管理

-------------------

# 简单的Flask测试网站
基于 Flask / Vue3 / Bootstrap / MySQL 开发

## 环境
* Python 3
* MySQL

## 快速开始

#### 1. 安装 Python 依赖
```sh
$ pip3 install -r requirements.txt
```

#### 2. 修改配置文件

根据自己情况，修改 `application/setting.cty`

主要是 `SQLALCHEMY_DATABASE_URI` 数据库的链接

```shell
$ export FLASK_DEMO_APPLICATION_SETTINGS=/Users/xulingjue/PycharmProjects/flask-demo/application/settings.cfg
```

#### 3. 创建数据库

根据上面配置中的库名，创建数据库

#### 4. 利用 flask-migrate 建表

命令行终端，先进入项目目录，然后依次执行下列命令：

```sh
$ export FLASK_APP=manage.py
# windows 系统：set FLASK_APP=manage.py

$ flask db init
$ flask db migratec
$ flask db upgrade
```

#### 5. 生成测试数据（可选）

可执行 [test_data.py](https://github.com/zkqiang/job-web-demo/blob/master/data/test_data.py) 生成一些随机数据



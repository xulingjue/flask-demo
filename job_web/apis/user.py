#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify

from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/api/helloworld')
def hello_world():  # put application's code here
    return 'Hello World!'


@user.route('/api/hello/<name>')
def hello_world1(name):  # hi
    return jsonify({'name': 'a', 'email': 'xulj09'});

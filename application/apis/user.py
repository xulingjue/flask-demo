#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

from .base_api import BaseApi
from ..models import User

user_api = Blueprint('user_api', __name__, url_prefix='/api/user')


@user_api.route('/', methods=['GET'])
def list():  # 获取用户列表
    users = User.query.all()
    return BaseApi().success_data(users)


@user_api.route('/api/user/<int:user_id>', methods=['GET'])
def info(user_id):  # 获取用户详情
    return jsonify({'name': 'a', 'email': 'xulj09'});

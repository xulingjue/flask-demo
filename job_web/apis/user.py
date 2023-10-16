#!/usr/bin/env python
# -*- coding: utf-8 -*-

from job_web.vendor.utils import Utils
from flask import Blueprint
from flask import jsonify

from ..models import User

user_api = Blueprint('user_api', __name__, url_prefix='/api/user')


@user_api.route('/', methods=['GET'])
def list():  # 获取用户列表
    users = User.query.all()
    return jsonify({'error_code': '200', 'data': Utils.db_l_to_d(users)})


@user_api.route('/api/user/<int:user_id>', methods=['GET'])
def info(user_id):  # 获取用户详情
    return jsonify({'name': 'a', 'email': 'xulj09'});


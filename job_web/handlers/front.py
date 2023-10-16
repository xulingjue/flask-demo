#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

front = Blueprint('front', __name__)


@front.route('/')
def index():
    return render_template('index.html', active='index')

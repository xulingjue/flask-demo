#!/usr/bin/env python
# -*- coding: utf-8 -*-

from application.main import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

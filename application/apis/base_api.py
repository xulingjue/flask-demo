from flask import request, jsonify

from application.main import app
from application.vendor.code import Code
from application.vendor.utils import Utils


class BaseApi:
    """
    * 返回成功信息
    * @param  msg string
    * @return json
    """

    def success_data(self, data='', msg='', show=True):
        return self.json({'error_code': Code.SUCCESS, 'data': Utils.db_l_to_d(data), 'msg': msg, 'show': show})

    """
    * 格式化返回值信息
    """

    def json(self, body={}):
        if app.config.get('DEBUG_LOG'):
            debug_id = Utils.unique_id()
            data = {
                'LOG_ID': debug_id,
                'IP_ADDRESS': request.remote_addr,
                'REQUEST_URL': request.url,
                'REQUEST_METHOD': request.method,
                'PARAMETERS': request.args,
                'RESPONSES': body
            }
            # 可以在此处增加log日志
            body['debug_id'] = debug_id
        return jsonify(body)

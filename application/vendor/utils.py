'''
author:hua
date:2018.5.9 工具类，封装一些通用方法
'''
import time


class Utils:
    '''
    * 用于sql结果列表对象类型转字典
    * @param list data
    * @return dict
    '''

    @staticmethod
    def db_l_to_d(data):
        data_list = []
        for val in data:
            val_dict = val.to_dict()
            data_list.append(val_dict)
        return data_list

    ''' 
    * 用于sql结果对象类型转字典
    * @param object obj
    * @return dict
    '''

    @staticmethod
    def class_to_dict(obj):
        '''把对象(支持单个对象、list、set)转换成字典'''
        is_list = obj.__class__ == [].__class__
        is_set = obj.__class__ == set().__class__
        if is_list or is_set:
            obj_arr = []
            for o in obj:
                # 把Object对象转换成Dict对象
                dict = {}
                dict.update(o.__dict__)
                obj_arr.append(dict)
                return obj_arr
        else:
            dict = {}
            dict.update(obj.__dict__)
            return dict

    """ uuid,唯一id 
        return string id
    """

    @staticmethod
    def unique_id(prefix=''):
        return prefix + hex(int(time.time()))[2:10] + hex(int(time.time() * 1000000) % 0x100000)[2:7]

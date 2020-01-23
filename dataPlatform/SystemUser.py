from tools.Dao import BaseService
import dataPlatform.sqlMapperPlatform as sqlMapper
from flask import jsonify, request, Blueprint

pfus = Blueprint("pfus", __name__)


# 做为服务的路由功能
@pfus.route('/pfus0001', methods=['GET'])
def pfus0001():
    '''用户登录'''
    request.service_id = 'pfus0001'
    dao_service = BaseService(request)

    # 获取初始化的参数
    # param = dao_service.param
    if not dao_service.param['error'] == '0':
        return dao_service.param

    sql = sqlMapper.check_sys_users_password
    temp = dao_service.select(sql=sql, param=dao_service.param)

    if not len(temp) == 1:
        dao_service.param['error'] = '用户名或密码错误!!!'
        return dao_service.param
    dao_service.param['user_id'] = temp[0][0]
    '''记录到登录日志中去'''
    dao_service.param['login_id'] = dao_service.get_uuid()

    sql = sqlMapper.insert_user_login_log
    a = dao_service.insert(sql=sql, param=dao_service.param)

    dao_service.commit_or_rollback()

    param = dao_service.return_param()

    return jsonify(param)


@pfus.route('/pfus0002', methods=['GET'])
def pfus0002():
    request.service_id = 'pfus0002'
    dao_service = BaseService(request)
    '''新增用户'''
    # 获取初始化的参数
    # param = dao_service.param
    if not dao_service.param['error'] == '0':
        return dao_service.param
    '''用户登录'''

    '''验证用户名和密码'''
    sql = sqlMapper.check_sys_user_phone_exist
    temp = dao_service.select(sql=sql, param=dao_service.param)
    if temp[0][0] == 1:
        dao_service.param['error'] = '手机号码不能重复!!'
        return dao_service.param

    dao_service.param['user_id'] = dao_service.get_uuid()

    sql = sqlMapper.insert_sys_user
    dao_service.insert(sql=sql, param=dao_service.param)

    dao_service.commit_or_rollback()
    param = dao_service.return_param()
    return jsonify(param)

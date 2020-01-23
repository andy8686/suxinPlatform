from tools.Dao import BaseService
import dataPlatform.sqlMapperPlatform as sqlMapper
from flask import jsonify,request,Blueprint

pfsm = Blueprint("pfsm",__name__)


@pfsm.route('/pfsm0001',methods=['GET'])
def pfsm0001():

    request.service_id = 'pfsm0001'
    dao_service = BaseService(request)
    # param = dao_service.param
    if not dao_service.param['error'] == '0':
        return dao_service.param

    '''查询服务 , 可以按照系统 或模块 或 服务ID查询'''
    sql = sqlMapper.get_service_by_id_or_module_sys
    a = dao_service.select(sql=sql, param=dao_service.param)
    if not len(a) > 0:
        dao_service.param['error'] = '没有查询到服务'
        return dao_service.param
    dao_service.param['list'] = a
    dao_service.param = dao_service.return_param()
    return jsonify(dao_service.param)

@pfsm.route('/pfsm0002',methods=['GET'])
def pfsm0002():
    request.service_id = 'pfsm0002'
    dao_service = BaseService(request)
    # param = dao_service.param
    if not dao_service.param['error'] == '0':
        return dao_service.param

    # '''新增服务'''
    # '''验证该模块是否存在'''
    a = {}  # 临时一个变量
    a['id'] = dao_service.param['sys_id'] + dao_service.param['module_id']
    sql = sqlMapper.get_module_by_id
    b = dao_service.select(sql=sql, param=a)
    if not len(b) == 1:
        dao_service.param['error'] = '模块或系统不存在!!!'
        return dao_service.param

    # '''取该模块最大的服务号'''
    sql = sqlMapper.get_maxid_in_a_module
    b = dao_service.select(sql=sql, param=self.param)
    if len(b) == 0:
        dao_service.param['new_service_id'] = '0001'
    elif len(b) == 1:
        # 如果该模块已经有了 , 那就加 1
        a = int(b[0][0]) + 1
        a = '0000' + str(a)
        dao_service.param['new_service_id'] = a[len(a) - 4:]
    # '''插入服务信息'''
    sql = sqlMapper.insert_service_infos
    dao_service.insert(sql=sql, param=dao_service.param)
    # if a.rowcount() == 1:
    #     self.param['error'] = '服务错误!!'
    dao_service.commit_or_rollback()

    dao_service.param = dao_service.return_param()
    return jsonify(dao_service.param)

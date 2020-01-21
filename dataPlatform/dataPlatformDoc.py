import tools.GlobalTools as gt

def get_flawgger_doc(service_id):
    flawgger_doc = gt.flasgger_template_doc_json
    in_param = gt.flasgger_template_doc_in_param
    out_param = gt.flasgger_template_doc_out_param
    if service_id == 'pfus0001':
        flawgger_doc['summary'] = '用户登录'
        flawgger_doc['description'] = '用户登录'
        in_param['phone'] = ['用户手机号码', '==11', 'int', '']
        in_param['password'] = ['用户密码', '>0', 'str', '']
        # ======================返回的参数=======================
        out_param['login_id'] = ['用户登录期间的ID']

    elif service_id == 'pfus0002':
        flawgger_doc['summary'] = '新增用户'
        flawgger_doc['description'] = '用户登录'
        in_param['phone'] = ['用户手机号码', '==11', 'int', '']
        in_param['password'] = ['用户密码', '>0', 'str', '']
        # ======================返回的参数=======================
        out_param['login_id'] = ['用户登录期间的']

    return gt.get_plus_paramsto_flawgger(flawgger_doc, in_param, out_param)


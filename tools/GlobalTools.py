import copy


def deep_copy(obj):
    '''# 深copy数据 ,
    传入的对象 LIST 其他需要转换'''
    return copy.deepcopy(obj)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



def plus_default_param_flawgger(param):
    for k, v in param.items():
        if len(v) < 1:
            param[k] = ['没有写注释']
        if len(v) < 2:
            param[k].append('==0')
        if len(v) < 3:
            param[k].append('str')
        if len(v) < 4:
            param[k].append('没写')

def get_plus_paramsto_flawgger(flawgger_doc, in_param, out_param):
    plus_default_param_flawgger(in_param)
    plus_default_param_flawgger(out_param)
    param_explain = {}
    param_length = {}
    param_type = {}
    param_example = {}
    for k, v in in_param.items():
        param_explain[k] = v[0]
        param_length[k] = v[1]
        param_type[k] = v[2]
        param_example[k] = v[3]

    flawgger_doc['description'] = '参数说明:' + str(param_explain)
    flawgger_doc['description'] += '''
参数长度:'''+ str(param_length)
    flawgger_doc['description'] += '''
参数类型:''' + str(param_type)
    flawgger_doc['parameters'][0]['description'] = '参数样例:' + str(param_example)

    for k, v in out_param.items():
        param_explain[k] = v[0]
        param_length[k] = v[1]
        param_type[k] = v[2]
        param_example[k] = v[3]

    flawgger_doc['responses']['200']['description'] = '参数说明:' + str(param_explain)
    flawgger_doc['responses']['200']['description'] += '''
参数长度:'''+ str(param_length)
    flawgger_doc['responses']['200']['description'] += '''
参数类型:''' + str(param_type)
    flawgger_doc['responses']['200']['examples']['param_example'] = str(param_example)

    return flawgger_doc

flasgger_template_doc_json = {
    "tags": ["平台模块"],
    "summary": "空空空",
    "parameters": [{"name": "传入参数",
                    "in": "body",
                    "type": "json",
                    "required": True,
                    "description": '后面生成'}],
    "schemes": ["http", "https"],
    "description": "用户登录介绍介绍!",
    "responses": {
        "200": {
            "description": "描述",
            "examples": {'param_example':''         }}}}
flasgger_template_doc_in_param = {'login_id': ['用户登录期间用于访问其它服务', '>0', 'str', '0']}
flasgger_template_doc_out_param = {'error': ['返回的错误问题,为零时服务正确!!', '>0', 'str', '0']}

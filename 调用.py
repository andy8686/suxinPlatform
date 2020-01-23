import requests, json

ip = '127.0.0.1:5000'
# ip = '192.168.98.15:80'

# service_id = 'pfus0001'
# param = {'phone': '13085000000', 'password': '13085000000'}

service_id = 'pfus0002'
param = {'phone': '13085000000', 'password': '13085000000',
         "login_id":"200121255-414c-a7d0-56d9de00b672",
'oldpassword': '13085000000', 'name': 'lisi',
'birthday': '20120908', 'sex': '0',
'email': '13093485@qq.com', 'account': '0'       }

# pfsm0001
# param = {'id': 'pf', 'login_id': '200114029-46c5-8efc-868f564bdd05'}

# pfsm0002
# param = {'sys_id': 'pf', 'module_id': 'sm',
#          'name':'测试模块',
#          'login_id': '200114029-46c5-8efc-868f564bdd05'}
# param['in_param'] = '''{"login_id":[">0","str"],"sys_id":[">0","str"],"module_id": ["==2", "str"], "name": [">6", "str"],"in_param": [">6", "str"],"out_param": [">0", "str"],"note": ["==0", "str"]}'''
# param['out_param'] = '''{"error":"值为0:表示注册成功,其他都是错误"}'''

data = requests.get('http://'+ip +"/"+service_id, json=param)
print(data.text)
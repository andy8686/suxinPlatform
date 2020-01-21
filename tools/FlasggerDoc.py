from tools.Dao import Dao
import dataPlatform.sqlMapperPlatform as sqlMapper
import json


class FlasggerDoc(object):
    flasggerDocJson = {
        "tags": [],
        "paths": {},
        "info": {
            "version": "1",
            "description": """python requests包调用的方式,以接口pfus0001 为例
            param = {'phone': '13085001100', 'password': '123'}
            requests.get('http://127.0.0.1:5000/pfus0001', json=param)   
            print(json.loads(data.text)) 
            
            传入参数说明 以以接口pfus0001 为例
            {"phone":["==11","int","用户登陆账号"] ,"password":[">6","str","用户密码"]}
            这里共有两个参数phone,password, 每个参数分别包含三个属性 以phone的为列 , 
            第一个:==11 代表传入的参数长度等于11 , 如果是 >10 也就是长度大于10 , 特别注意如果是==0 那就是不限制,
            第二个:int 代表传入的参数类型 ,有 str,int, date(后面是格式化的样式例如:dateyyyymmdd=date('参数',yyyymmdd)) """,
            "title": "接口调用说明",
            "termsOfService": "http://www.suxin.thce",
            "contact": {
                "email": "13085001100@qq.com"
            }
        },
        "schemes": [
            "https",
            "http"
        ],
        "swagger": "2.0"
    }

    def init_flasgger_json_doc(self):
        dao = Dao()
        self.param = {"id": "all"}

        sql = sqlMapper.get_module_by_id
        modules = dao.select(sql=sql, param=self.param)
        if len(modules) < 0:
            self.param['error'] = '服务ID错误!!!'
            return self.param
        module = {}
        for m in modules:
            self.flasggerDocJson['tags'].append({"name": m[0] + m[1]})
            module[m[0]] = m[0] + m[1]

        self.param = {"id": "all"}
        sql = sqlMapper.get_service_by_id_or_module_sys
        services = dao.select(sql=sql, param=self.param)
        if len(services) < 0:
            self.param['error'] = '服务ID错误!!!'
            return self.param

        for ss in services:
            paths = {}
            paths["tags"] = [module[ss[0][0:4]]]
            paths["summary"] = ss[1]
            paths["parameters"] = [{
                "in": "query",
                "name": "json",
                "type": "string",
                "description": ss[2],
                "required": True}]
            paths["responses"] = {
                "200": {
                    "description": ss[3]
                }}
            self.flasggerDocJson["paths"]["/" + ss[0]] = {"get": paths}

        with open("tools\\flasggerDoc.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(self.flasggerDocJson, ensure_ascii=False))

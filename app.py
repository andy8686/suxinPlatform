from flask import Flask, request, render_template, jsonify
import tools.ServiceRoute as sroute
# from dataPlatform.SystemUser import pfus
from tools.FlasggerDoc import FlasggerDoc
from flasgger import Swagger
app = Flask(__name__)

# 返回中文
app.config['JSON_AS_ASCII'] = False
# app.register_blueprint(pfus)

@app.route('/')
def index():
    return jsonify({"错误的网址":"0"})

@app.route('/<service_id>')
def service(service_id):
    request.service_id = service_id
    # 调用路由处理服务
    params = sroute.invoke(request)
    return jsonify(params)

@app.before_request
def before_request_handle():
    print('每次请求之前都执行')
    return

@app.after_request
def allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://example.com'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

    return response

flasggerDoc = FlasggerDoc()
flasggerDoc.init_flasgger_json_doc()
swag = Swagger(app,template_file="tools\\flasggerDoc.json")

if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    # app.run(host='192.168.98.15', port=80, debug=True)
    app.run(debug=True)






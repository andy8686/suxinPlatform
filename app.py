from flask import Flask, request, render_template, jsonify
from dataPlatform.SystemUser import pfus
from dataPlatform.ServiceManage import  pfsm
from tools.FlasggerDoc import FlasggerDoc
from flasgger import Swagger
app = Flask(__name__)

# 返回中文
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(pfus)
app.register_blueprint(pfsm)


@app.route('/')
def index():
    return render_template("index.html")

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






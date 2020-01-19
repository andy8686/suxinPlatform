from flask import Flask, request, render_template
from dataPlatform.dataPlatFormRoute import pf_blue
from flasgger import Swagger
app = Flask(__name__)

app.register_blueprint(pf_blue)

# '''对外提供微服务执行的代码'''
# @app.route('/<service_id>.do' ,methods=['GET', 'POST'])
# def to_service(service_id):
#     # 平台系统的调用platform
#     # request.service_id = service_id
#     # out_param = pf.invoke(request)
#
#     # return jsonify(out_param)
#     pass
#
# @app.route('/')
# def index():
#     return render_template("index.html")
#

@app.errorhandler(404)
def err_404_handler(err):
    #err 错误的信息
    return render_template("index.html")
    pass

@app.before_request
def before_request_handle():
    requesta = request
    print(requesta.url)
    print('每次请求之前都执行')

# @app.after_request
# def after_request_handle(response):
#     print('每次请求之后执行')
#     # return response
#
# @app.teardown_request
# def teardown_request_handle(err):
#     print('每次请求之后执行,错误是',err)

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['title'] = '接口文档'
swagger_config['description'] = '''接口文档调用描述
python requests包调用的方式,以接口pfus0001
param = {'phone': '123', 'password': '123'}
requests.get('http://127.0.0.1:5000/pfus0001', json=param)

ajax调用的方式注意 dataType , 和返回参数
param = {'phone': '123', 'password': '123'}
$.ajax({url: 'http://127.0.0.1:5000/pfus0001',
        data: params,
        async: false,
        dataType: 'json',
        cache: false,
        success: function (data, textStatus, jqXHR) {
            retFunc.success(data);
            retData = data;
            //retFfunc.success(data);        }    })
'''

swag = Swagger(app,config=swagger_config)
if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    # app.run(host='192.168.98.15', port=80, debug=True)
    app.run(debug=True)

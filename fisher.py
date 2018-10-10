from app import create_app

app = create_app()

from app.web import book

if __name__ == '__main__':
    # print('id为' + str(id(app)) + '启动')
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

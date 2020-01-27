from flask import Flask, request, Response
# from api import models
from flask_restful import Api
from api.resources import DeveloperResource


app = Flask(__name__)
api = Api(app)

api.add_resource(DeveloperResource, '/developers', '/developers/<string:dev_id>')






















# @app.route('/developers', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def hello_world():

    # if request.method == 'GET':

    #     object = models.Developer.objects.to_json()
    #     return Response(object, mimetype='application/json')

    # elif request.method == 'POST':
    #     models.Developer(
    #         **request.get_json(),
    #         ).save()
    #     return Response(status=201)

    # elif request.method == 'PUT':
    #     pass

    # elif request.method == 'DELETE':
    #     pass









if __name__ == '__main__':
    app.run(debug=True)
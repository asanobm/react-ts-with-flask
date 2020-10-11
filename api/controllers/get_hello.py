from api import app
import json


@app.route('/hello', methods=['GET'])
def get_movies():
    # return Response(Response=json.dumps({'message': 'hello'}))

    return json.dumps({'message': 'hello world'})

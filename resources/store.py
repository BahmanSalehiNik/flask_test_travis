from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'new_name',
        required=True,
        help='This field can not be empty'
    )

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message': f'store with name {name} not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f'a store with name {name} already exists'}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
            return {'message': f'store with name {name} successfully saved'}, 201

        except Exception as e:
            return {'message': f'something went wrong: {str(e)}'}, 500

    def put(self, name):
        data = Store.parser.parse_args()
        new_name = data['new_name']
        store = StoreModel.find_by_name(name)
        if store:
            store.store_name = new_name
            store.save_to_db()
            return {'message': f'store name: {name} changed to {new_name}'}

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        store.delete_from_db()
        return {'message': f'store with name {name} successfully deleted'}


class StoreList(Resource):
    def get(self):
        return {'message': [store.json() for store in StoreModel.query.all() ]}, 200

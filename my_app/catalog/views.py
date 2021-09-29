from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.catalog.models import Catalog

catalog = Blueprint('catalog', __name__)

@catalog.route('/')
@catalog.route('/home')
def home():
    return "Welcome to the catalog Home."

class CatalogViewRequests(MethodView):
    def post(self):
        data = request.form
        name = data.get('name')
        image = data.get('image')
        description = data.get('description')
        link = data.get('link')

        catalog = Catalog(name, image, description, link)
        db.session.add(catalog)
        db.session.commit()

        return jsonify({
            catalog.id: {
                'id': catalog.id,
                'name': catalog.name,
                'image': catalog.image,
                'description': catalog.description,
                'link': catalog.link,
            }
        })


class CatalogView(MethodView):

    def get(self, id=None, page=1):
        _list = []
        if not id:
            catalogs = Catalog.query.paginate(page, 20).items
            for catalog in catalogs:
                catalog_dict = {
                    'id': catalog.id,
                    'name': catalog.name,
                    'image': catalog.image,
                    'description': catalog.description,
                    'link': catalog.link,
                }
                _list.append(catalog_dict)
        else:
            catalog = Catalog.query.filter_by(id=id).first()
            
            if not catalog:
                abort(404)
            
            catalog_dict = {
                'id': catalog.id,
                'name': catalog.name,
                'image': catalog.image,
                'description': catalog.description,
                'link': catalog.link,
            }

            _list.append(catalog_dict)

        return jsonify({'data': _list})

    def post(self):
        data = request.form
        name = data.get('name')
        image = data.get('image')
        description = data.get('description')
        link = data.get('link')

        catalog = Catalog(name, image, description, link)
        db.session.add(catalog)
        db.session.commit()

        return jsonify({
            'data': {
                'id': catalog.id,
                'name': catalog.name,
                'image': catalog.image,
                'description': catalog.description,
                'link': catalog.link,
            } 
        })

    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return

    def delete(self, id):
        # Delete the record for the provided id.
        catalog = Catalog.query.filter_by(id=id).first()
        db.session.delete(catalog)
        db.session.commit()
        return jsonify({'message': 'Success'})


catalog_view_requests = CatalogViewRequests.as_view('catalog_view_requests')
catalog_view = CatalogView.as_view('catalog_view')

app.add_url_rule(
    '/catalog/',
    view_func=catalog_view,
    methods=['GET', 'POST']
)

app.add_url_rule(
    '/catalog/<int:id>',
    view_func=catalog_view,
    methods=['GET', 'DELETE']
)
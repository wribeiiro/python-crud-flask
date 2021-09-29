from my_app import db

class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    
    def __init__(self, name, image, description, link):
        self.name = name
        self.image = image
        self.description = description
        self.link = link

    def __repr__(self):
        return '<Catalog %d>' % self.id

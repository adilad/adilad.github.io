from  app import app
from flask_frozen import Freezer

freezer = Freezer(app)

@freezer.register_generator
def index():
    yield '/'

if __name__ == '__main__':
    freezer.freeze()

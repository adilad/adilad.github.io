from  app import app
from flask_frozen import Freezer

freezer = Freezer(app)

@freezer.register_generator
def index():
    yield '/'
@freezer.register_generator
def mystory():
    yield '/mystory.html'

if __name__ == '__main__':
    freezer.freeze()

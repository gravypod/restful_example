from os import getenv

from waitress import serve
from restful_example import app

serve(app=app, host=getenv('ADDRESS', '0.0.0.0'), port=int(getenv('PORT', '80')))

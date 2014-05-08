import sae
from photowall import wsgi

application = sae.create_wsgi_app(wsgi.application)
from aiohttp import web
import aiohttp_jinja2
import jinja2
from application.routes import setup_routes
from application.settings import config,BASE_DIR
from application.middleware import setup_middlewares

app = web.Application()
setup_routes(app)
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'templates')))
setup_middlewares(app)
app['config'] = config
web.run_app(app, host='127.0.0.1', port=9000)
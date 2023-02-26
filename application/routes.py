from aiohttp import web
from .views import articles,handler,hello,add_user,json_handler
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent

def setup_routes(app):
    routes = [
        web.get('/', handler),
        web.get('/welcome', hello),
        web.get('/articles', articles),
        web.post('/add_user', add_user),
        web.post('/jsontest', json_handler),
        web.static('/static/', path=PROJECT_ROOT / 'static', name='static')
    ]
    app.router.add_routes(routes)
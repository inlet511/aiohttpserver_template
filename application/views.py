from aiohttp import web
import aiohttp_jinja2

async def handler(request):
    print('New paged visited')
    return web.Response(text='MainPage')

async def hello(request):
    return web.Response(text='hello')

async def add_user(request):
    data = await request.post()
    username = data.get('username')
    # add user in database
    return web.Response(text=f"{username} was added")


async def json_handler(request):
    args = await request.json()
    data = {'value':args['key']}
    return web.json_response(data)

@aiohttp_jinja2.template('index.html')
async def articles(request):
    return {"articles":[
                {"title":"文章1"},
                {"title": "文章2"},
                {"title": "文章3"}]}
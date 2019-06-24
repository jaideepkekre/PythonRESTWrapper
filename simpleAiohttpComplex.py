import uvloop
import asyncio
import aiohttp
from aiohttp import web
routes = web.RouteTableDef()

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy()


@routes.get('/')
async def hello(request):
    async with app['http_session'].get('https://jsonplaceholder.typicode.com/posts/1') as resp:
        pass
    async with app['http_session'].get('https://jsonplaceholder.typicode.com/posts/2') as resp:
        pass
    async with app['http_session'].get('https://jsonplaceholder.typicode.com/posts/3') as resp:
        pass
    async with app['http_session'].get('https://jsonplaceholder.typicode.com/posts/4') as resp:
        pass
    return web.Response(text="Hello, world")


async def stup(app):
    app['http_session'] =  aiohttp.ClientSession()

async def stop(app):
    await app['http_session'].close()
app = web.Application()
app.on_startup.append(stup)
app.on_cleanup.append(stop)
app.add_routes(routes)
web.run_app(app, port=8787)

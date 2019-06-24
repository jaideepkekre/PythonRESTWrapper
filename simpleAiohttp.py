from aiohttp import web
routes = web.RouteTableDef()
import aiohttp
import asyncio
import requests
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())



@routes.get('/')
async def hello(request):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts/1') as resp:
            pass
        async with session.get('https://jsonplaceholder.typicode.com/posts/2') as resp:
            pass
        async with session.get('https://jsonplaceholder.typicode.com/posts/3') as resp:
            pass
        async with session.get('https://jsonplaceholder.typicode.com/posts/4') as resp:
            pass
    return web.Response(text="Hello, world")





async def sync_work(url):
    x=11
    while x > 0 :
        await asyncio.sleep(0)
        requests.get(url)
        x=x-1


app = web.Application()
app.add_routes(routes)
# web.run_app(app, port=8787)

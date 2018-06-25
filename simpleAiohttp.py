from aiohttp import web
routes = web.RouteTableDef()
import math
@routes.get('/')
async def hello(request):
    print(math.factorial(234))
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes(routes)
web.run_app(app,port=8282)
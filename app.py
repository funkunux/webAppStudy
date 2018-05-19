import aiohttp
import asyncio
from aiohttp import web


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://www.baidu.com')
        print(html)


async def delayLoop(time):
    while True:
        result = await asyncio.sleep(time, "await %fs..." % time)cd
        
        print(result)


routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)

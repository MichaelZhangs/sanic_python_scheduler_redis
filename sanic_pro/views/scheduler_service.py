from settings import app
from sanic.views import HTTPMethodView
from sanic.response import json
import threading
import datetime

class Book(HTTPMethodView):

    def send_hello(self, *args):
        print(f"{args[0]}: welcome you ....")


    async def post(self, request):
        data = request.json
        user_id = data.get("user_id")
        t = datetime.datetime.now()
        exe_time = t + datetime.timedelta(seconds=10)
        # print(exe_time)
        # exe_time = datetime.datetime.strptime(str(exe_time).split(".")[0], "%Y-%m-%d %H:%M:%S")
        app.scheduler.add_job(self.send_hello, trigger="date",  next_run_time=exe_time , args=(user_id,), id=user_id, replace_existing=True )

        return json({"ok": 1})

    async def get(self, request):

        data = request.args
        user_id = data.get("user_id")
        t = datetime.datetime.now()
        exe_time = t + datetime.timedelta(minutes=2)
        # print(exe_time)
        # exe_time = datetime.datetime.strptime(str(exe_time).split(".")[0], "%Y-%m-%d %H:%M:%S")
        app.scheduler.add_job(self.send_hello, trigger="date", jobstore="redis", next_run_time=exe_time , args=(user_id,), id=user_id, replace_existing=True )

        return json({"status": 200})


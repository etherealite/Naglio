from bottle import route, run
from multiprocessing import Process
import time

@route('/')
def index():
    return 'service check web interface'

kw_args = {'host':'localhost', 'port':8080}
p = Process(target=run, kwargs=kw_args)
p.start()
#p.join()
#run(host='localhost', port=8080)


from bottle import route, run
import time
problems = 0
message = ""
@route('/')
def index():
    return 'problems {} <br> {}'.format(problems, message)



from bottle import route, run

@route('/')
def index():
    return 'service check web interface'

run(host='localhost', port=8080)

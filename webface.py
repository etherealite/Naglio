from bottle import route, run

@route('/')
def index(name='World'):
    return 'shityy'

run(host='localhost', port=8080)

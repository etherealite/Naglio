@route('/')
def index():
    return 'problems {} <br> {}'.format(problems, message)



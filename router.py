from _lib.bottle import route, run, template, static_file, abort, redirect


@route('/static/<path:path>')
def host_static(path):
    return static_file(path, root='./static/')


@route('/')
def index():
    return static_file('./md/index.md', root='./')


@route(r'/index<:re:\..*>')
def redirect_to_index():
    redirect('/')


@route('/md/<name>.md')
def view_md(name):
    path = './md/' + name + '.md'
    return static_file(path, root='./')


@route(r'/md/<name:re:[^\.].*$>')
def path_to_view(name):
    # md_path = './md/' + name + '.md'
    # with open(md_path) as md_file:
    #    md_text = md_file.read()
    #    print(md_text)
    return template('sample', name=name)
    # return static_file('./md/' + name, root='./')


@route('/restricted')
def restricted():
    abort(401, 'Sorry, access denied.')


if __name__ == "__main__":
    run(host='localhost', reloader=True, debug=True)

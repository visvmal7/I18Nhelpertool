import web

urls = (
    '/', 'index',)

app = web.application(urls, globals())

render = web.template.render("c:/projects/gothonweb/templates/")


def GET():
    greeting = 'Hello world!'
    return render.index(greeting=greeting)


class index(object):
    # GET takes the value and display POST is to enter value in runtime
    pass


if __name__ == "__main__":
    app.run()

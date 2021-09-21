import web

urls = (
    '/', 'index',)

app = web.application(urls, globals())

render = web.template.render("c:/projects/gothonweb/templates/")


def GET():
    form = web.input(name="Nobody")
    greeting = "Hello, %s" % form.name
    return render.index(greeting=greeting)


class index(object):
    pass


if __name__ == "__main__":
    app.run()

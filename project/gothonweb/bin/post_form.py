import web

# Below commented line, if you want to manually provide manually paramenter on webpage
# to display what you want
# urls = (
# '/item', 'index','/MainPage','MainPage')
urls = (
    '/item', 'index')

app = web.application(urls, globals())

render = web.template.render("c:/projects/gothonweb/templates/", base="layout")


def POST():
    form = web.input(name="Vishal", greet="Welcome")
    greeting = " %s %s" % (form.name, form.greet)
    return render.index_laid_out(greeting=greeting)


def GET():
    return render.hello_form_laid_out()

## Below commented one is to different webpage, to call this you have to manually givea parameter
## for e.g localhost:/8080/MainPage
# class MainPage(object):
#     def GET(self):
#         greeting = "Trial practise"
#        return render.index(greeting = greeting)


class index(object):
    pass


if __name__ == "__main__":
    app.run()

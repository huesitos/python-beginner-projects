import web


urls = (
    '/(.*)/(.*)', 'hello'
)

render = web.template.render("resources/")
app = web.application(urls, globals())


class hello:
    def GET(self, name, age):
        if not name:
            name = "World"
        return render.main(name, age)


if __name__ == "__main__":
    app.run()

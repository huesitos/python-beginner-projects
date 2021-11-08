import web
from models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates",
                             base="MainLayout",
                             globals={'session': session_data, 'current_user': session_data["user"]})


# Classes/Routes
class Home:
    def GET(self):
        data = type('obj', (object,), {"username": "denisselara", "password": "123456"})

        login = LoginModel.LoginModel()
        is_correct = login.check_user(data)

        if is_correct:
            session_data["user"] = is_correct

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        return render.Home(posts)


class Login:
    def GET(self):
        return render.Login()


class Register:
    def GET(self):
        return render.Register()


class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return True


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        is_correct = login.check_user(data)

        if is_correct:
            session_data["user"] = is_correct
            return is_correct

        return 'error'


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"


class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"


if __name__ == "__main__":
    app.run()

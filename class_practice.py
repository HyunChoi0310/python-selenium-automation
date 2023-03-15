class Base:
    def __init__(self):
        self.url = 'www.amazon.com'

    def open_url(self):
        print('Opening url', self.url)

    def close(self):
        print('url closed', self.url)

class LoginBase(Base):
    def open_login(self):
        self.open_url()

    def close_login(self):
        self.close()
b = Base()

b.open_url()
b.close()
print(b.url)

login = LoginBase()

login.close_login()
print(login.url)
login.open_url()
login.close()

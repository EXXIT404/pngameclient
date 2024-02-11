#import requests

class User :
    def __init__(self):
        self.loggedIn = False

    # def login(self, username, password) -> bool:
    def login(self, loggedIn=True):
        self.loggedIn = loggedIn
        self.name = "test"
        self.id = 69
        self.coins = 3141592
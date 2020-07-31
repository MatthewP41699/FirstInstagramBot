from instapy import InstaPy
from InstabotGUI import *
global session

def VerifyUser(username, password):
     session = InstaPy(username, password, headless_browser= True)
     session.login()
     print("Login Successful")
     
def followbytags(tags, dontliketags):
     print("Following Users:")
     session.like_by_tags(tags, amount =5)
     session.set_dont_like(dontliketags)
     session.end()
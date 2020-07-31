from tkinter import *
from InstaBot import *
import os


class LoginScreen(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		usernameLabel= Label(self, text = "Username")
		username = StringVar()
		usernameBox = Entry(self, textvariable = username)

		passwordLabel = Label(self, text = "Password")
		password = StringVar()
		passwordBox = Entry(self, textvariable = password, show= "*")

		#result = loginVerification(username, password)
		loginButton= Button(self, text= "Enter Username and Password", command = lambda: loginVerification(usernameBox.get(), passwordBox.get()))

		usernameLabel.grid(row = 1, column = 0)
		usernameBox.grid(row=1, column=1)
		passwordLabel.grid(row = 2, column = 0)
		passwordBox.grid(row=2, column=1)
		loginButton.grid(row =5, column =0)

	def closeWindow(self):
		self.master.destroy()

class OptionWindow(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):

		optionLabel = Label(self, text = "Choose would you like to view the people followed by the app?").grid(row=0, column = 0)
		spaceLabel = Label(self, text = " ").grid(row = 1, column = 0)

		followLabel= Label(self, text="Enter tags you would like to follow(seperate with commas):").grid(row = 2)
		tags = StringVar()
		tagstofollowEntry = Entry(self, textvariable = tags).grid(row = 3)

		spaceLabel.grid(row = 3)

		dontFollow = Label(self, text="Enter tags you would not like to follow(seperate with commas):").grid(row = 4)
		dontfollowtags = StringVar()
		tagsnottofollowEntry = Entry(self ,  textvariable = dontfollowtags).grid(row = 5)

		followbytags(splitEntries(tags), splitEntries(dontfollowtags))

		followLabel = Label(self, text = "Accounts followed in this session:").grid(row = 2)



#need to use InstaBot to check to see if username and password are correct
def loginVerification(username ,password): 
	print(username ,",", password)
	VerifyUser(username, password)
	loginPage.withdraw()
	root.iconify()
	OptionWindow(root)
	root.mainloop()

def splitEntries(tag):
	taglist = (tag.get()).split(',')
	return taglist

root=Tk()
root.withdraw()
root.geometry("400x400")
root.title("First Instagram Bot")

loginPage = Toplevel(root)

#Error is given in extension.xpi exists. We must delete
#if(os.path.isfile('C:\\Users\\matth\\InstaPy\\assets\\extension.xpi')):
#	os.remove(os.path('C:\\Users\\matth\\InstaPy\\assets\\extension.xpi'))

LoginScreen(loginPage)
root.mainloop()





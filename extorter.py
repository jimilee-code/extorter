'''
drag every social media someone might have
based on input information (like a survey form)
you do not have to fill in all categories to perform the search
'''
import tkinter
import time
import requests
import json

X_RapidAPI_Key = "*"

def main():
	global X_RapidAPI_Key
	def insta_display(fn, un, pfp, pk):
		# display information and picture
		# split into grids and then put in pictures
		'''
		instawindow = tkinter.Tk() ; instawindow.geometry("500x700") ; instawindow.title("_______s3arch r3sults_______")
		for i in range(int(len(fn)/2)):
			for j in range(2):
				frame = tkinter.Frame(master=instawindow, borderwidth=1)
				frame.grid(row=i, column=j)
				label = tkinter.Label(master=instawindow, text=f"Row {i} Column {j}")
				label.place(x=0,y=100)
				'''
		return 0

	def handle_submit():
		global X_RapidAPI_Key ; full_name = [] ; username = [] ; profile_pic_url = [] ; country_in_feed = [] ; country_in_profile = [] ; pk = []
		url_insta_search = "https://instagram-data1.p.rapidapi.com/user/search"
		firstn = firstname.get()
		lastn = lastname.get()
		phonen = phonenum.get()
		email1_ = email1.get()
		email2_ = email2.get()
		email3_ = email3.get()
		# API section
		if firstn=='' and lastn=='': # if neither first or last names were entered
			pass
		else: 
			headers = {"X-RapidAPI-Host":"instagram-data1.p.rapidapi.com","X-RapidAPI-Key":X_RapidAPI_Key}
			if firstn=='':
				if lastn!='': # if only last name was entered
					params={"keyword":str(lastn)}
					insta_search_response = requests.get(url_insta_search, headers=headers, params=params)
					print(insta_search_response.text)
			elif firstn!='':
				if lastn=='': # if only first name was entered
					params={"keyword":str(firstn)}
					insta_search_response = requests.get(url_insta_search, headers=headers, params=params)
					print(insta_search_response.text)
				else: # if both first and last names were entered
					params={"keyword":str(firstn)+' '+str(lastn)}
					insta_search_response = requests.get(url_insta_search, headers=headers, params=params)
					insta_search_response_text = insta_search_response.text ; print(insta_search_response_text)
					insta_search_response_list = json.loads(insta_search_response_text) # convert to list
					for i in range(len(insta_search_response_list)):
						full_name.append(insta_search_response_list[i]['user']['full_name'])
						username.append(insta_search_response_list[i]['user']['username'])
						profile_pic_url.append(insta_search_response_list[i]['user']['profile_pic_url'])
						if insta_search_response_list[i]['user']['has_primary_country_in_profile'] == True:
							pass # what to do when country is listed
						if insta_search_response_list[i]['user']['has_primary_country_in_profile'] == True:
							pass # ''
						pk.append(insta_search_response_list[i]['user']['pk'])
					insta_display(full_name, username, profile_pic_url, pk)


	basewindow = tkinter.Tk() ; basewindow.title('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
	basewindow.geometry("380x250")
	basetitle = tkinter.Label(text="per$on $earch", foreground="red", background="black", font=("Arial", 18)).pack()
	firstname_label = tkinter.Label(text="First Name", foreground="white", background="black").place(x=0, y=50)
	firstname = tkinter.Entry(width=15) ; firstname.place(x=70, y=50)
	lastname_label = tkinter.Label(text="Last Name", foreground="white", background="black").place(x=0, y=75)
	lastname = tkinter.Entry(width=15) ; lastname.place(x=70, y=75)
	phonenum_label = tkinter.Label(text="Phone #", foreground="white", background="black").place(x=0, y=98)
	phonenum = tkinter.Entry(width=15) ; phonenum.place(x=70, y=98)
	email1_label = tkinter.Label(text="Email #1", foreground="white", background="black").place(x=0, y=121)
	email1 = tkinter.Entry(width=30) ; email1.place(x=70, y=121)
	email2_label = tkinter.Label(text="Email #2", foreground="white", background="black").place(x=0, y=144)
	email2 = tkinter.Entry(width=30) ; email2.place(x=70, y=144)
	email3_label = tkinter.Label(text="Email #3", foreground="white", background="black").place(x=0, y=167)
	email3 = tkinter.Entry(width=30) ; email3.place(x=70, y=167)

	submit = tkinter.Button(basewindow, text="$earch", font=("Arial", 12), background="black", foreground="red", bd=10, command=handle_submit)
	submit.place(x=300, y=200)
	#submit.bind("<Button-1>", handle_submit)

	basewindow.mainloop()

main()

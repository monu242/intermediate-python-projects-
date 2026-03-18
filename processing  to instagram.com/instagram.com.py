# we are making  a code to visit instagram,and searching something on insta using python.(basic url code)


import webbrowser#researched about how to use webbrowser module in python and now using it 


query = input("what you want to search on instagram [-_-]:")#taking input from user

url = f"https://www.instagram.com/explore/search/keyword/?q={query}"

webbrowser.open(url)#using this  to opening the url in webbrowser module to work in real browser
#this  will open instagram and search  user input from query 

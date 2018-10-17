#Split up a URL of the form http://www.something.com (Listing 2-2 page 29 0f book)

domain = url[11:-4]
url = input('Please enter the URL:')

print("Domain name: " + domain)
print()

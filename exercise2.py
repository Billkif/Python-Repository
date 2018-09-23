#Split up a URL of the form http://www.something.com

domain = url[11:-4]
url = input('Please enter the URL:')

print("Domain name: " + domain)

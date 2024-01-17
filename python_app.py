#collect the email from the user
#split the email using the @, the first part as the username and the second part as the domain
#split the email using the ., the first part as the domain and the second part as the extension
def main():
    print("Welcome to the email slicer \n")

    email_input = input("Input your Email Address: ")
    (username, domain) = email_input.split('@')
    (domain, extension) = domain.split('.')

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()
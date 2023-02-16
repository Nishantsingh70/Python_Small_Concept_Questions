#Get the user's email address.
# strip() will remove spaces in the begining and end of email address.
email = input('What is your email address?: ') .strip()

#Slice out the user name
user_name = email[: email.index('@')]

#Slice out the domain name
domain_name = email[email.index('@')+1:]

#Format message
res = "your username is '{0}' and your domain name is '{1}'".format(user_name,domain_name)

#Display the result message
print(res)
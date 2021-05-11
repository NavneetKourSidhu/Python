email = input("What is your email address: ").strip()

user_name = email[:email.index("@")]

domain_name = email[email.index("@")+1:]

output = f"Username is '{user_name}' and domain name is '{domain_name}'"

print(output)

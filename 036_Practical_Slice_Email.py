# ----------------------------
# --Practical Slice Email --
# ----------------------------


name = input ("What's your name ? ").strip().capitalize()
email = input ("what's your email ? ").strip()

ussername = email [: email.index ("@")]
domain = email [email.index ("@") + 1 : email.index (".") ]

print (f"Hello {name} \nYour email is {email} \nYour username is {ussername} \nYour domain is {domain} ")

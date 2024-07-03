import re

def validate_email_syntax(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    ma=re.match(pattern,email)
    if ma:
        print("Correct")
    else:
        print("Incorrect")
def validate_phone(phone):
    pattern=r"[6-9][0-9]{9}$"
    ma=re.match(pattern,phone)
    if ma:
        print("Correct Mobile number")
    else:
        print("Incorrect mobile no")
validate_email_syntax("mahenderudutala@gmail.com")
validate_phone("1712345694")
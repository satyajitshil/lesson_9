med_cond = input("Is your medical condition Y or N:")
attend = int(input("What is your attendance:"))
if med_cond == "Y":
    print("You are allowed")
else:
    if attend >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")
        
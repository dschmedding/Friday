def greeting(name, gender):
    if gender == "m":
        prefix = "Mr."
    elif gender == "f":
        prefix = "Mrs."
    else:
        prefix = ""
    print("Hello {} {}, how are you?".format(prefix, name))
    print("My name is Daniel")
    print("It is my pleasure to be working with you")

person = input("Who are you? ")
gender = input("What is your gender ")
greeting(person, gender)







with open("credentials.txt", "r") as file:
    text = file.read().split("\n")

    if len(text) != 2:
        print("Invalid Format")
        raise TypeError()
    
    USERNAME = text[0]
    PASSWORD = text[1]
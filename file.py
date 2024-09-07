

def argumenFile(password):
    file = 'yourpasswords.txt'
    with open(file, "w") as object_file:
        for p in password:
            object_file.write(p)

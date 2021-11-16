my_list = input("Please enter a list of numbers or words seperated by spaces: ")

choice = input("Do you want the ends or the middle? ")

split = my_list.split(" ")

if choice == "ends":
    del split[1:len(split) - 1]
    print(split)
if choice == "middle":
    split = [split [0], split[len(split) - 1]]
    print(split)

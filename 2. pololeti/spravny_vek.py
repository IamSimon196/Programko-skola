

postup = False
while not postup:
    age = input("Zadej svuj vek cisli:\n")
    
    if age.isdecimal():
        postup = True
    else:
        print("Pouze cela cisla")


postup = False
while not postup:
    password = input("Zadej heslo(pouze cisla a pismena):\n")

    if password.isalnum():
        postup = True
    else:
        print("pouze cisla a pismena")

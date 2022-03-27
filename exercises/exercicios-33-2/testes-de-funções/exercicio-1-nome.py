def vertical_name(name):
    try:
        idx = len(name)
        while idx > 0:
            red = ''
            index_letter = 0
            while index_letter < idx:
                red += name[index_letter]
                index_letter += 1
            print(red) 
            idx -= 1

    except TypeError:
        print("precisa de ser um nome válido") 



vertical_name(1)
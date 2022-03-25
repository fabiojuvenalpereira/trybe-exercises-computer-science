name_list = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]

def the_biggest_name(names):
    last_biggest = ""

    for name in names:
        if len(name) >= len(last_biggest):
            last_biggest = name

    return last_biggest

print(the_biggest_name(name_list))

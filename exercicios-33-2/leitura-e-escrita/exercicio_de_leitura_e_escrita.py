

try:
    nomes = (open("names.txt", mode="r").read().split())
    ind_nome, ind_note = 0, 1

    list_names_and_note = []

    while ind_nome < len(nomes):
        tupla = (nomes[ind_nome], int(nomes[ind_note]))
        list_names_and_note.append(tupla)
        ind_nome, ind_note = ind_nome + 2, ind_note + 2

    try:
        new_archive = open("reproved_list.txt", mode="w")
        
        reproved = [ f"{student[0]}\n"
                    for student in list_names_and_note
                    if student[1] < 6]
        print(new_archive.writelines(reproved))
    except:
        print("não foi possível gerar o arquivo")

except:
    print("não foi possível ler arquivo, ou arquivo inexistente")
    
finally:
   new_archive.close()
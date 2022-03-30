class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

meu_user = User("Fabio", "fabio@gmail.com", "senha")

print(meu_user)
print(meu_user.name)
print(meu_user.email)
print(meu_user.password)
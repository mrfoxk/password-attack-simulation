

# Este script serve pra pegar a saida do comando de enumeracao de usuarios do smb
# e criar uma saida para um arquivo de senhas

with open("saida_enumeracao_samba.txt", "r") as f:
  linhas = f.readlines()

usuarios = []

for linha in linhas:
  if "Account: " in linha:
    parte = linha.split("Account:")[1]
    usuario = parte.split()[0]
    usuarios.append(usuario)

with open("smb_users.txt", "w") as arquivo:
    for y in usuarios:
        arquivo.write(y + "\n")

print("Completo.")

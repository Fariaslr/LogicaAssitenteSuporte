from usuario import Usuario

u = Usuario()

u.nome = input("Olá, qual é o seu nome: ")

while(True):
  u.opcao = input(u.nome+" necessita de qual suporte?\n1 - Suporte técnico\n2 - Suporte financeiro"
                 "\n3 - Suporte administrativo\n4 - Suporte comercial\n5 - Suporte TI: ")
  
  match int(u.opcao):
      case 1:
          print("Olá,", u.nome, "seu suporte técnico está aqui!")
          break
      case 2:
          print("Olá,", u.nome, "seu suporte financeiro está aqui!")
          break 
      case 3:
          print("Olá,", u.nome, "seu suporte administrativo está aqui!")
          break 
      case 4:
          print("Olá,", u.nome, "seu suporte administrativo está aqui!")
          break
      case 5:
          print("Olá,", u.nome, "seu suporte administrativo está aqui!")
          break
      case _:
          print("Valor inválido!")
  
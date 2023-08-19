print("Atividade de Produção - Laboratório de Programação\nMozart Lemos de Siqueira\n\n***********************************************\n")

arquivo = open("ativprod.txt", "r") #para ler o arquivo e ler a quantidade de caracteres.
conteudo = arquivo.read()
num_caracteres = len(conteudo)
print("* O arquivo possui um total de", num_caracteres, "caracteres.\n")

arquivo = open("ativprod.txt","r") #para ler o arquivo e mostrar no console.
print(arquivo.readlines())

print("\n***********************************************\n")

arquivo = open("ativprod.txt", "a") # para incluir o texto no fim do arquivo.
arquivo.write("*****TEXTO NA ÚLTIMA LINHA: Aluno Jeferson da Silveira Rosa \ Matrícula 202221001*****")

arquivo = open("ativprod.txt","r") #para ler o arquivo e mostrar no console.
print(arquivo.readlines())

arquivo = open("ativprod.txt", "r") #para ler o arquivo e ler a nova quantidade de caracteres.
conteudo = arquivo.read()
num_caracteres = len(conteudo)
print("\n* Agora o arquivo possui um total de", num_caracteres, "caracteres.")

arquivo = open("ativprod.txt", "w") #para voltar ao texto original sem a adição da última linha
arquivo.write("TAREFA:Entregar um fonte em Python para manipular um arquivo previamente existente. Para os testes, use este arquivo da descrição do trabalho e salve com texto.txt.O programa deve abrir, ler o conteúdo do arquivo e mostrar, contar o número de caracteres e inserir uma frase e salvar (digitada pelo usuário do programa) no final do arquivo.")

arquivo.close()

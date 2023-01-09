
#--------- strings ---------

print('ola mundo') # função responsável por escrever algo no terminal

print("ola mundo") # Strings podem ser armazenadas em aspas simples e aspas duplas

print('ola' + 'mundo') # na função print diferentes strings podem ser concatenadas com o  caractere '+'

print('ola' , 'mundo') # na função print diferentes strings podem ser concatenadas com o  caractere ',' e vão ser separadas por um espaço ' '

#-------- números e strings -----------

print( 7 + 4 ) # a conta será realizada e printada na tela

print( '7' + '4' ) # a conta não será realizada e os numeros serao considerados strings e concatenados

print( 7 , 4 ) # a conta não será realizada e os numeros serão considerados strings e printados separados por um espaço ' '

# print( '7' + 4 ) não funciona pois a função não concatena um tipo String com tipo int

# ---------------- variáveis ------------------

# todas as variáveis para python são consideradas objetos

nome = 'João Prado'
idade = 21
peso = 90.0

print(nome, idade, peso)

#-------------- entradas e interação com usuário --------------

nome = input('qual é seu nome? ')

idade = input('qual é sua idade? ')

peso = input('qual é seu peso? ')

print(nome, idade, peso)
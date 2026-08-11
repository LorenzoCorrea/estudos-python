# # 1 - Liste valores de 0 a 10 que sejam menor que 4;;
# for i in range(10):
#   if i <4:
#     print(i)

listNumbers = [i for i in range(10) if i <4]
print(listNumbers)


gamesList = ["Mario" , "Red Dead", "Spider-Man","Kirby", "Dispatch"]

# 2 - jogos que possuem a letra A
newList = [x for x in gamesList if "a" in x]
print(newList)



# 3 - jogos que não zerei
gamesFinished = [x for x in gamesList if x != "Kirby"]
print(gamesFinished)
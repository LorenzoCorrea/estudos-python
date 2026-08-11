class Movie: ###Sempre nomear a classe com a primeira letra maiuscula
  name = ""
  yearLaunch = 0
  includedPlan = False
  note = 0
  durationMinutes = 0
  

# Primeiro Filme #
movie = Movie()
movie.name = "Super man"
movie.yearLaunch = 2024
movie.includedPlan = False
movie.note = 5.0
movie.durationMinutes = 170
print("### Dados do Filme ###")
print(f"Nome do filme: {movie.name} \n Ano de Lançamento:{movie.yearLaunch}")



# Segundo filme #

movie2 = Movie()
movie2.name = "Spider man"
movie2.yearLaunch = 2026
movie2.includedPlan = False
movie2.note = 5.0
movie2.durationMinutes = 250
print("### Dados do Filme ###")
print(f"Nome do filme: {movie2.name} \n Ano de Lançamento:{movie2.yearLaunch}")


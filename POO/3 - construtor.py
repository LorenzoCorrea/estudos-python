class Movie:
  def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
    self.name = name
    self.yearLaunch = yearLaunch
    self.includedPlan = includedPlan
    self.note = note
    self.durationMinutes = durationMinutes


movie = Movie("Super man", 2024, False, 5.0, 120)
print(movie.name)
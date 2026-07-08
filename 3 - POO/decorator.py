def my_decorator(func):
  def wrapper():
    print("Antes de excetura a função")
    func()
    print("Depois de executar a função")
  return wrapper
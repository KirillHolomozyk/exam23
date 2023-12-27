def arimethmetic_progression(a, d, n):
    #a: Перший член прогресії
    #d: Постійний член прогресії
    #n: Номер елемента прогресії

  return a + (n - 1) * d


def main():

  a = 5
  d = 2
  n = int(input("Введіть номер елемента: "))

  print("Значення п-го елемента прогресії:", arimethmetic_progression(a, d, n))


if __name__ == "__main__":
  main()
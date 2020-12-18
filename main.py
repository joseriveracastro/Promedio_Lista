def promedio(l_nota):
  prom = sum(l_nota)/len(l_nota)
  nota_menor = min(l_nota)
  nota_mayor = max(l_nota)
  cantidad_notas = len(l_nota)
  suma_notas = sum(l_nota)
  return prom, nota_menor,nota_mayor,cantidad_notas,suma_notas


lista = [2,3,4,2,5,3,5]

estudiante = promedio(lista)

print(estudiante[0])
print(estudiante[1])
print(estudiante[2])

print(f'El promedio del estudiante {estudiante[0]} y la cantidad de notas {estudiante[3]}')
import numpy as np
from sympy import *
from DataIn import set_val

def show_tl(tl):
  x,y,z,a,b,c,d,e,f,g,h,i = symbols('x y z a b c d e f g h i')
  char = [x,y,z,a,b,c,d,e,f,g,h,i]
  expresion = []
  for i in range(len(tl)):
    cadena = []
    aux = 0
    for j in range(len(tl[0])):
      aux += char[j]*round(tl[i][j])
    expresion.append(aux)
  print(expresion)

def primeraValidacion(u,v):
  v = np.copy(u)
  uv = np.array([0 for i in range(len(u))])
  result = u+v
  for i in range(len(u)):
    uv[i] = u[i] + v[i]
  if np.array_equal(result,uv):
    return True
  return False

def segundaValidacion(u):
  alpha = -1
  result = alpha*u
  for i in range(len(u)):
    u[i] = u[i]*alpha
  if np.array_equal(result,u):
    return True
  return False

def find_tl(u,v):

  results = []
  for i in range(len(v[0])):
    result = []
    for j in range(len(v)):
      result.append(v[j][i])
    results.append(result)

  for result in results:
    result = np.array(result)

  sistema_eq = []
  for vector in u:
    equation = []
    for i in range(len(u)):
      equation.append(vector[i])
    sistema_eq.append(equation)
  sistema_eq = np.array(sistema_eq)

  tl = []
  for result in results:
    aux = np.linalg.solve(sistema_eq,result)
    tl.append(np.ndarray.tolist(aux))
  print("La transformacion lineal es la siguiente")
  show_tl(tl)

def main():
  u,v = set_val()
  if u != 0 and v != 0:
    tl = True
    for i in range(len(u)):
      a = np.array(u[i])
      b = np.array(v[i])
      if not(primeraValidacion(a,b) and segundaValidacion(a)):
        tl = False
    if(tl):
      print("Es una transformacion lineal")
      find_tl(u,v)
    else:
      print("No es una transformacion lineal")

main()
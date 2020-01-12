from calculadora import Calculadora
from comodo import Comodo
calc = Calculadora()

print(
    'Esta aplicação tem como finalidade calcular a área das paredes e teto de um ambiente e informar a quantidade de tinta necessária para o cômodo em questão.\n'
)

comodo = Comodo(
    input('Qual a largura do cômodo? '),
    input('Qual a profundidade do cômodo? ')
)

print(
    "A área das paredes é:  ",
    calc.calcular_area_paredes(comodo)
)

print(
    'A área do teto é: ',
   calc.calcular_area_teto(comodo)
)

print(
    'A litragem de tinta necessária é: ',
    calc.calcular_litragem_necessaria()
)
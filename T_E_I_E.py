def triangulos(A,B,C):
  if A <= 0 or B <= 0 or C <= 0:
    triangulo = False
  elif A > (B + C) or B > (A + C) or C > (A + B):
    triangulo = False
  else:
    if A == B and B == C:
        #LOGO A = C
      isoceles = False
      escaleno = False
      triangulo = True
      equilatero = True
    elif A == B != C or A == C != B or A == C != B or B == C != A:
      triangulo = True
      equilatero = False
      isoceles = True
      escaleno = False
    else:
      triangulo = True
      equilatero = False
      isoceles = False
      escaleno = True
  return triangulo, equilatero, isoceles, escaleno


while True:
    try:
        print('MENU.')
        print('DESCUBRA O TRIANGULO!')
        print('PARA INICIAR: [1] PARA SIM / [QUALQUER TECLA] PARA NÃO.')
        mn = int(input('DESEJA INICIAR?: '))
        if(mn == 1):
            x = 0
            count = 0
            while(count < 100):
                x += 1
                print('-'*56)
                print('CALCULE O TRIANGULO INSERINDO DADOS.')
                print('PARA CANCELAR A OPERAÇÃO APERTE QUALQUER TECLA QUE NAO SEJE UM NUMERO.')
                print('-'*56)
                A = float(input('Digite o valor do lado A do triângulo (ex: 5,06): '))
                B = float(input('Digite o valor do lado B do triângulo (ex: 9,32): '))
                C = float(input('Digite o valor do lado C do triângulo (ex: 5,06): '))
                triangulo, equilatero, isoceles, escaleno = triangulos(A,B,C)
                print(f'Triângulo número {x}')
                print(f'É um triângulo? {triangulo}')
                print(f'Esse triângulo é equilátero? {equilatero}')
                print(f'Esse triângulo é isóceles? {isoceles}')
                print(f'Esse triângulo é escaleno? {escaleno}')
        else:
            print('EXIT')
            break
    except:
       print('EXIT')
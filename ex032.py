retaA = float(input('digite a reta 1: '))
retaB = float(input('digite a reta 2: '))
retaC = float(input('digite a reta 3: '))

retaVerify1 = (retaB - retaC) < retaA < retaB + retaC
retaVerify2 = (retaA - retaC) < retaB < retaA + retaC
retaVerify3 = (retaA - retaB) < retaC < retaA + retaB

if retaVerify1 == 1 and retaVerify2 == 1 and retaVerify3 == 1:
    print("Essas retas podem formar um triangulo")
else:
    print("Essas retas não podem formar um triangulo")




def add_fraction(fraction1, fraction2):
    num1, dnum1 = fraction1
    num2, dnum2 = fraction2
    return num1*dnum2 + num2*dnum1, dnum1 * dnum2
    
def sub_fraction(fraction1, fraction2):
    num1, dnum1 = fraction1 
    num2, dnum2 = fraction2
    return num1*dnum2 - num2*dnum1, dnum1 * dnum2

def mult_fraction(fraction1, fraction2):
    num1, dnum1 = fraction1 
    num2, dnum2 = fraction2
    return num1*dnum2, dnum1*num2

def div_fraction(fraction1, fraction2):
    num1, dnum1 = fraction1 
    num2, dnum2 = fraction2
    return num1*dnum2, dnum1*num2



num1 = int(input("Entrez votre numerateur1 ")
dnum1 = int(input("Entrez votre denumerateur1 "))
num2 = int(input("Entrez votre numerateur2 "))
dnum2 = int(input"Entrez denumerateur2 ")

fract1 = num1, dnum1
fract2 = num2, dnum2

n1, d1 = add_fraction(fract1, fract2)

print(f'{n1}/{d1}')





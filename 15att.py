ph=float(input('quanto vc ganaha por hora:'))
ht=float(input('quantas horas vc trabalhou esse mes:'))
sb=ph*ht
ir=sb*(11/100)
inss=sb*(8/100)
sin=sb*(5/100)
sl=sb-ir-inss-sin
print('salario bruto{}\n ir (11%): R${}\n inss (8%): R${}\n sin (5%): R${}\n salario liguido:R${}'.format,(sb,ir,inss,sin,sl))
import math
mq=float(input('digite quantos metros vc vai pintar'))
lt=math.ceil(mq/54)
pr=lt*80
print('vc precisara de {}latas de tnt,custando R${}'.format(lt,pr))

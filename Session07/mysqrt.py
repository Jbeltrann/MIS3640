


epsilon = 0.0000001 
def mysqrt(a):
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
          break
        x = y
    return y
    
#mysqrt(100)
import math
def test_square_root():
    print('a   mysqrt(a)     math.sqrt(a)  diff')
    print('-   ---------     ------------  ----')
    for i in range(9):
        i +=1
        a = i
        b = mysqrt(a)
        c = math.sqrt(a)
        d = abs(b-c)
        print('{:.1f} {:.10f}  {:.10f}  {}'.format(a, b, c, d))



        
test_square_root()
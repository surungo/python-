import os
import sys
import operator

def criar(xi,xf,yi,yf):
 if yi == yf+1:
  return
 else:
  if xi == xf+1:
   return (criar(0,xf,yi+1,yf))
  else:
   print("x",xi," y",yi)
   return (criar(xi+1,xf))

criar(0,3,0,2)


#def main(arg):
#    print(arg)

#main(sys.argv[1])
n = len(sys.argv)
print(n)
print(sys.argv[1])

print(operator.add(1,1))
newDir='newDir'
curDir = os.getcwd()
print(curDir)
#if os.path.exists(newDir):
# os.rmdir(newDir)
if True!=os.path.exists(newDir):
 os.mkdir(newDir)
dir_list = os.listdir(curDir)
print(dir_list)

if os.path.exists(newDir):
 os.rmdir(newDir)



print('hi')
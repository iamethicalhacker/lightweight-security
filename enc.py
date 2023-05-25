import random
import string
key="abab"

a=13
def trans(x):
    d={
        "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24," ":25
    }
    return d.get(x,"invalid")
def rtrans(x):
    rd={
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",
        16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:" "

    }
    return rd.get(x,"invalid")
m = 2
n = 2
def cipher(st,key,a,m,n):
  
  def trans(x):
    d={
        "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24," ":25
    }
    return d.get(x,"invalid")
  def rtrans(x):
    rd={
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",
        16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:" "

    }
    return rd.get(x,"invalid")
  def matrixAddition(matA,matB,m,n):
    outputMat = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            sum = matA[i][j]+matB[i][j]
            row.append(sum)
        outputMat.append(row)

    return outputMat

  def matrixmult(matA,m,n,a):
    outputMat = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            sum = (matA[i][j])*a
            row.append(sum)
        outputMat.append(row)

    return outputMat
  def matrixmod(matA,m,n):
    outputMat = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            sum = (matA[i][j])%26
            row.append(sum)
        outputMat.append(row)
    return outputMat

  def displayMatrix(matX,m,n):
    for i in range(0,m):
        print(matX[i])


#key_l=int(input("enter length of key: "))
#res=''.join(random.choices(string.ascii_letters,k=key_l))
#print("key is: " +  str(res))
#print(res)
  def createMatrix(m,n,st):
    outputMat = []
    k=0
    for i in range(0,n):
        row = []
        for j in range(0,m):
            inp = (trans((st[k])))
            k=k+1
            row.append(inp)
        outputMat.append(row)

    return outputMat


  matA = []
  matB = []
  matC = []

  print(f"Enter all the {m*n} elements of Matrix A down below: \n")
  matA = createMatrix(m,n,st)

  print(f"Enter all the {m*n} elements of Matrix B down below: \n")
  matB = createMatrix(m,n,key) #res
  print("\n Matrix A \n")
  displayMatrix(matA,m,n)
  print("\n Matrix B \n")
  displayMatrix(matB,m,n)

  print("\n encryption \n")

  print("The sum of matrices A & B is: \n")
  print("\n Matrix C \n")
  matC1 = matrixAddition(matA, matB, m, n)
  matC=matrixmod(matC1,m,n)
  displayMatrix(matC,m,n)

  print("\n Matrix D  \n")
  matD1 = matrixmult(matC,m,n,a)
  matD=matrixmod(matD1,m,n)
  displayMatrix(matD,m,n)


  def rcreateMatrix(m,n,s):
    s12=""
    
    for i in range(0,n):
        
        for j in range(0,m):
            inp = str(rtrans((s[i][j])))
            s12=s12+inp
        

    return s12

  y=rcreateMatrix(m,n,matD)
  
  return y



def hill(st,key,a):
   if len(st)%4!=0:
    p=int(len(st)/4)
    mk=4*(p+1)-len(st)
    for i in range(mk):
     st=st+" "
   print(st)

   st1=""
   ci=""
   i=0
   while i<len(st):
      st1=(st[i:i+4])
      ci1=cipher(st1,key,a,m,n)
      ci=ci+ci1
      ci1=""
      i=i+4
   print(ci)
   return ci
      
      





def h(st):
 
 return hill(st,key,a)

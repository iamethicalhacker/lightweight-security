import random
import string

m=int(input("col:"))
n=int(input("row:"))
def di(ci,key,a,m,n):

 np=a 
 p=26
 mp=1
 while(((p*mp)+1)%np)!=0:mp=mp+1
 b=int(((p*mp)+1)/np)

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
 def matrixmult(matA,m,n,a):
    outputMat = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            sum = (matA[i][j])*a
            row.append(sum)
        outputMat.append(row)

    return outputMat

 def matrixsubtraction(matA,matB,m,n):
    outputMat = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            sum = matA[i][j]-matB[i][j]
            if sum<0:
                sum=sum+26
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

 matA=[]
 matB=[]
 matA = createMatrix(m,n,ci)
 matB = createMatrix(m,n,key)
 displayMatrix(matA,m,n)
 print("\n Matrix B \n")
 displayMatrix(matB,m,n)
 def rcreateMatrix(m,n,s):
    s12=""
    
    for i in range(0,n):
        
        for j in range(0,m):
            inp = str(rtrans((s[i][j])))
            s12=s12+inp
    return s12

 print("\n Matrix E \n")
 matE1= matrixmult(matA,m,n,b)
 matE=matrixmod(matE1,m,n)
 displayMatrix(matE,m,n)


 print("\nMatrix F \n")
 matF = matrixsubtraction(matE,matB,m,n)
 displayMatrix(matF,m,n)

 s123=rcreateMatrix(2,2,matF)
 return s123

def hill(st,key,a):
   if len(st)%4!=0:
    p=int(len(st)/4)
    mk=4*(p+1)-len(st)
    for i in range(mk):
     st=st+" "
    print(st)
   st1p=""
   cip=""
   i=0
   while i<len(st):
      st1p=(st[i:i+4])
      ci1p=di(st1p,key,a,m,n)
      cip=cip+ci1p
      ci1p=""
      i=i+4
   
   print(cip)
      
      


hill("mckmqjnt","jiok",5)
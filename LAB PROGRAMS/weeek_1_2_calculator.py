r = int(input("enter rows"))
c = int(input("enter columns"))
A = []
for i in range(r) :
    x = []
    for j in range(len(A)) :
        x.append(int(input("Enter the value")))
    A.append(x)
for i in range(r) :
   A=[[1,2],[3,4]]
   B=[[1,2],[3,4]]
   C=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        C[i][j]=A[i][j]+B[i][j]


for i in C:
    print(i)
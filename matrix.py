import  numpy as  np

def solve(A,B):
    if np.linalg.det(A) == 0:
        return []
    coeff_m = np.matrix(A)
    rhs = np.matrix(B)
    rhs = rhs.getT()
    A_inv = np.linalg.inv(A)
    return A_inv @ B

n = int(input("enter number of variables :"))

A=[]; B=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(float(input("Enter the coefficient of "+str(j+1)+"th variable in equation "+str(i+1)+" :")))
    A.append(temp)
for i  in range(n):
    B.append(float(input("Enter RHS of equation "+str(i+1)+" :")))
res = solve(A,B)

if  len(res)==0:
    print("No solution exists")
else :
    print("the solution is :")
    print(res)
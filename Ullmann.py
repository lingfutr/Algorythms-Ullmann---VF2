import networkx as nx
import numpy as np

##########################################
"""
A,B - матрицы смежности
pa,pb - кол-во вершин в графах
"""


def read_matrix_from_file(file):
    """
    :param file: 
    :return: 
    """
    fin=open(file)
    n=int(fin.readline())
    matrix=[]
    for i in range(n):
        s=fin.readline().split(" ")
        sint=[int(i) for i in s]
        matrix.append(sint)
    return matrix

def output_matrix_to_file():
    pass



def show_matrix(matrix):
    """
    :param matrix: 
    :return: 
    """
    for i in range(len(matrix)):
        print(matrix[i])


def vect_mul(vect1, vect2):
    """
    :param vect1: 
    :param vect2: 
    :return: 
    """
    if len(vect1)==len(vect2):
        cnt=0
        for i in range(len(vect1)):
            cnt+=vect1[i]*vect2[i]
        return cnt


def row(matrix,number):
    """
    :param matrix: 
    :param number: 
    :return: 
    """
    return matrix[number]


def column(matrix,number):
    return [matrix[i][number] for i in range(len(matrix))]


def mul_matrix(matrix1,matrix2):
    """
    :param matrix1: 
    :param matrix2: 
    :return: 
    """
    matrix=[]
    for i in range(len(matrix1)):
        matrix.append([])
        for j in range(len(matrix2)):
            matrix[i].append(vect_mul(row(matrix1,i),column(matrix2,j)))
    return matrix

def transpose_matrix(matrix):
    """
    :param matrix: 
    :return: 
    """
    copy=matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]=copy[j][i]
    return matrix

def condition1(matrix1,matrix2):
    """
    :param matrix1: 
    :param matrix2: 
    :return: True or False respectively 
    """
    n=len(matrix1)
    for i in range(n):
        for j in range(n):
            if matrix1[i][j]==1:
                if matrix2[i][j]!=1:
                    return False
    return True


def deg(matrix, point):
    """
    :param matrix: 
    :param point: 
    :return: 
    """
    cnt=0
    for i in range(len(matrix)):
        if matrix[point][i]==1:
            cnt+=1
    return cnt

def m0_init(A,B):
    """
    :param A: 
    :param B: 
    :return: 
    """
    matrix=[]
    m=len(A)
    n=len(B)
    for i in range(m):
        matrix.append([])
        for j in range(n):
            if deg(B,i)>=deg(A,j):
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix

"""
def condition2(matrix1,matrix2,matrixM):
    pa=len(matrix1)
    pb=len(matrix2)
    for i in range(pa):
        if matrix1[&][i]==1:
            for j in range(pb):
                if matrixM[i][j]*matrix2[y][??]==1:
                    return True
    return False
"""


def employing_refinement_procedure():
    pass


#H,F=[0 for i in range(pa)],[0 for i in range(pb)]
#либо в виде словарей
#H,G={},{}

file1 = 'C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1'
file2 = 'C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph2'



A=read_matrix_from_file(file1)
B=read_matrix_from_file(file2)

M0=m0_init(A,B)
"""
show_matrix(M0)
C=mul_matrix(M0,transpose_matrix(mul_matrix(M0,B)))

D=[]
D.append([0,0,0,1])
D.append([0,1,0,0])
D.append([0,0,1,0])
D.append([1,0,0,0])

C=mul_matrix(D,transpose_matrix(mul_matrix(D,B)))
print()
show_matrix(M0)
print(condition1(C,A))
show_matrix(C)
"""


def my_condition(matrix):
    for i in range(len(matrix)):
        if row(matrix,i).count(1)!=1:
            return False
    return True



M=M0
H=[]
G={}
d=0
Mcopy=M.copy()

def Ull(A,B):
    global d,M,Mcopy

    if my_condition(M):
        C=mul_matrix(M,transpose_matrix(mul_matrix(M,B)))
        if condition1(C,A):
            return M
    if d < len(M):
        for i in range(len(M)):
            if M[d][i]==1 and i not in G.values():
                G[d]=i
                for j in range(i+1,len(M)):
                    M[d][j]=0
#        show_matrix(M)
            else:
                M[d][i]=0
        d+=1
        Ull(A,B)
    else:
        d-=1
        for j in range(len(M)):
            M[d][j]=Mcopy[d][j]
        Ull(A,B)
    #return M



M01=transpose_matrix(read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\M01"))
M02=transpose_matrix(read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\M02"))
M03=transpose_matrix(read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\M03"))
M04=transpose_matrix(read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\M04"))

C=mul_matrix(M01,transpose_matrix(mul_matrix(M01,B)))
print(condition1(C,A))
C=mul_matrix(M02,transpose_matrix(mul_matrix(M02,B)))
print(condition1(C,A))
C=mul_matrix(M03,transpose_matrix(mul_matrix(M03,B)))
print(condition1(C,A))
C=mul_matrix(M04,transpose_matrix(mul_matrix(M04,B)))
print(condition1(C,A))
print()

"""
Ull(A,B)
show_matrix(M)
C=mul_matrix(M,transpose_matrix(mul_matrix(M,B)))
print(condition1(A,C))

"""

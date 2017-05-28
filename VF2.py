import networkx as nx



#################################
def read(file):
    G = nx.Graph()
    fin = open(file)
    n = int(fin.readline())
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        s = fin.readline().split(' ')
        for j in range(i-1, n):
            if s[j] == '1':
                G.add_edge(i, j)
    return G



file1 = 'C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1'
file2 = 'C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph2'


G1=read(file1)
G2=read(file2)
#################################

mapping=set()#???


#здесь вычисляется множество P(s)
def M(s):
    """
    :param s: state 
    :return:  P(s) - set posible pairs to add in mapping
    """
    return
    pass

def Match(s):
    """
    This procedure input intermediate state s
    and output mapping between two graph
    """


    if len(M(s)) == len(G2.nodes()):
        return M(s)
    else:
        P(s)# for inclusion in M(s)
    for p in P(s):
        if feasibility_rules==True:# for inclusion of p in M(s):
            s1= M(s).add(p)
            Match(s1)
##    Restore Data structure



def P(s):
    """
    input intermidiate state
    and compute candidate for inclusion in mapping
    """
    pass


def feasibility_rules(s, n, m):
    return (Fsyn(s, n, m) and Fsem(s, n, m))


def Fsyn(s, n, m):
    return (Rpred() and Rsucc and Rin and Rout and Rnew)



def Fsem(s, n, m):
    ##    n~m and for i in M(s): for j in B1: if (n,n`)~(m,m`) and for
    pass




#Функция, возвращает множество предков для вершины n из графа G, если
def Pred(G, n):
    pass

#Функция, из множества Set возвращает список по фильтру - множеству куда должен входить кандидат
def exist(Set,Filter):
    ans=[i for i in Set if i in Filter]
    return ans







#Проверка предшественников
def Rpred(s, n, m):         #s-текущее состояние, n и m - кандидаты на добавление в отображение
    """
    :param s: intermediate state 
    :param n: candidate from G1
    :param m: candidate friom G2
    :return:  True or False respectively
    """
    M1=M.copy()
    M2=M.copy()
    for i in (M1.update(Pred(G1,n))):    #n` заменена на i
        if (exist(Pred(G2,m))) not in M(s):  #m` заменена на j
            return False

    for i in (M2.update(Pred(G2, m))):  # n` заменена на i
        if (exist(Pred(G1, n))) not in M(s):  # m` заменена на j
            return False

    return True


#Проверка наследников
def Rsucc(s, n, m):
    pass


def Rin(s, n, m):
    pass


def Rout(s, n, m):
    pass


def Rnew(s, n, m):
    pass


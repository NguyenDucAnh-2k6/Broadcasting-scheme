from ortools.sat.python import cp_model
import sys
def Input():
    f=sys.stdin
    [n,m,s,L]=[int(x) for x in f.readline().split()]
    Out={}
    for v in range(1,n+1):
        Out[v]=[]
    for _ in range(m):
        [u,v,t,c]=[int(x) for x in f.readline().split()]
        Out[u].append([v,t,c])
        Out[v].append([u,t,c])
    return n,m,s,L,Out
def inputfile(filename):
    with open(filename, 'r') as f:
        [n,m,s,L]=[int(x) for x in f.readline().split()]
        Out={}
        for v in range(1,n+1):
            Out[v]=[]
        for _ in range(m):
            [u,v,t,c]=[int(x) for x in f.readline().split()]
            Out[u].append([v,t,c])
            Out[v].append([u,t,c])
    return n,m,s,L,Out
#n,m,s,L,Out=Input()
n,m,s,L,Out=inputfile('Multicast routing data.txt')
A=[]
for i in range(1,n+1):
    for [j,t,c] in Out[i]:
        if j!=s:
            A.append([i,j,c])
model=cp_model.CpModel()
x={}  #x[i,j]
y={}  #time to reach node
for i in range(1,n+1):
    for [j,t,c] in Out[i]:
        x[i,j]=model.NewIntVar(0,1,'x['+str(i)+','+str(j)+']')
for i in range(1,n+1):
    y[i]=model.NewIntVar(0,1000000, 'y['+str(i)+']')
#Processing => by boolean
for i in range(1,n+1):
    for [j,t,c] in Out[i]:
        b=model.NewBoolVar('b')
        model.Add(x[i,j]==1).OnlyEnforceIf(b)
        model.Add(x[i,j]!=1).OnlyEnforceIf(b.Not())
        model.Add(y[j]==y[i]+t).OnlyEnforceIf(b)
#Flow balance
for j in range(1,n+1):
    if j!=s:
        model.Add(sum(x[i,j] for [i,t,c] in Out[j])==1)
model.Add(y[s]==0)
#Time max
for i in range(1,n+1):
    model.Add(y[i]<=L)
#Define obj
model.Minimize(sum(x[i,j]*c for [i,j,c] in A))
solver=cp_model.CpSolver()
solver.parameters.max_time_in_seconds=10.0
status=solver.Solve(model)
if status==cp_model.OPTIMAL or status==cp_model.FEASIBLE:
    print('Optimal cost: ', int(solver.ObjectiveValue()))
    for [i,j,c] in A:
        if solver.Value(x[i,j])>0:
            print('Selected ', i, j)
else:
    print('NO_SOLUTION')
    
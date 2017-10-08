def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

# f(2) => [0,1] here it refers to new clock of memory
# f(3,[3,2,1]) =>[3,2,1,0,1,4] here it refers to new clock of memory
# f(3) => [0,1,0,1,4] because it referes to the same block of memory as the first one

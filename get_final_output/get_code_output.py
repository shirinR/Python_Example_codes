def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

# f(2) => [0,1] here it refers to new clock of memory
# f(3,[3,2,1]) =>[3,2,1,0,1,4] here it refers to new clock of memory
# f(3) => [0,1,0,1,4] because it referes to the same block of memory as the first one

# NOTE: another way of coding above code
# l_mem = []
#
# l = l_mem           # the first call
# for i in range(2):
#     l.append(i*i)
#
# print(l)            # [0, 1]
#
# l = [3,2,1]         # the second call
# for i in range(3):
#     l.append(i*i)
#
# print(l)            # [3, 2, 1, 0, 1, 4]
#
# l = l_mem           # the third call
# for i in range(3):
#     l.append(i*i)
#
# print(l)            # [0, 1, 0, 1, 4] 

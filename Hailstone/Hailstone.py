def hailstone_seq(x):
    x_list=[x]
    while True:
        if x%2==0:
            x=x//2
        else:
            x=3*x+1
        x_list.append(x)
        if x==1:
            return x_list

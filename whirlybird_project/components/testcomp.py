

def EngHrs(We, V, Q):
    a = 4.86
    b = 0.777
    c = 0.894
    d = 0.163


    mat = [a, b, c, d]
    

    He = a * We**(b) * V**(c) * Q**(d)
    return print('Engineering Hours:', He)

EngHrs(1, 2, 3)

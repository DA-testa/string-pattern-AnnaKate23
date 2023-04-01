# python3

d=256
q=101

def read_input():
    print("Input 'I' or 'F': ")
    text = input()
    if "I" in text:
        P = input().rstrip()
        T = input().rstrip()
        if len(P) < 1:
            print("Error")
        if len(T) < len(P):
            print("Error")
        if len(T) > 5*(10**5)
            print("Error")
        return P, T
    elif "F" in text:
        with open(f"./test/{file}", "r") as filee:
            P = file.readline().rstrip()
            T = file.readline().rstrip()
        return P, T

    

    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(P, T):
    M = len(P)
    N = len(T)
    i=0
    j=0
    pp=0
    tt=0
    h=1

    for i in range(M-1):
        h = (h*d)%q

    for i in range(M):
        pp = (d*pp + ord(P[i]))%q
        tt = (d*tt + ord(T[i]))%q

    occurances = []
    for i in range(N-M+1):
        if pp == tt:
            for j in range(M):
                if T[i+j] != P[j]:
                    break
            j = j+1
            if j == M:
                occurances.append(i)
        if i < N-M:
            tt = (d*(tt-ord(T[i])*h) + ord(T[i+M])) % q
            if tt<0:
                tt = tt + q
    return occurances


    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


#Working through leetcode
#Fibonacci sequence problem 

def fib(self, N):
    if N == 0:
        return 0 
    elif N == 1:
        return 1 
    elif N == 2:
        return 1 
    elif N > 2:
        return self.fib(N-1) + self.fib(N-2)
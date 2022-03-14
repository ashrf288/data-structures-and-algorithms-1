def fibonacci_recurion(n):
    pass





def fib(n):
	seq=[0,1]
	i = 2
	while i<=n:
		seq.append(seq[i-1]+seq[i-2])
		i+=1
	return seq[n]

if __name__=='main':
    
print(fib(5))
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)  

print(fibonacci(5))


"""
Line 7: This line contains the recursive logic. It calls the fibonacci function twice:
fibonacci(n - 1): This call computes the Fibonacci number for the position one less than n.
fibonacci(n - 2): This call computes the Fibonacci number for the position two less than n.
The results of these two calls are added together and returned as the output. This implements the Fibonacci formula: 
F
(
n
)
=
F
(
n
−
1
)
+
F
(
n
−
2
)
F(n)=F(n−1)+F(n−2).

"""
def fibonacci(n):
    if fib_dict[n]:
        return fib_dict[n]
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
      next = fibonacci(n-1) + fibonacci(n-2)
      fib_dict[n] = next 
      return next
   

input_object=open("input3.txt","r")
output_object=open("output3.txt","w")
num = int(input_object.readline())
fib_dict={i:[] for i in range (num+2)}
f = fibonacci(num+1)
output_object.write((str(f)))


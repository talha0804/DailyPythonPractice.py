def checkprime(num):
      count=0
      i=2
      while i<=num:
           if num % i==0:
              count+=1 
           i+=1
       
      if count==1:
           print("Prime Number")
      else:
           print("Not a Prime Number")
           
  

x=int(input("Enter a number:"))
checkprime(x)
    
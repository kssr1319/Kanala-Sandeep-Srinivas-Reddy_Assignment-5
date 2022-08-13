# Write a Python class to implement pow(x, n)
# Explanation:
# Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)
# You must implement it using Class

# Sample Input:
# x: 10
# n: 2
# Sample Output:
# 100

class pow:
   def power(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.power(x,-n)
        r = self.power(x,n//2)
        if n%2 ==0:
            return r*r
        return r*r*x

x=int(input("Enter base value :"))
n=int(input("Enter power value :"))
print("power of (x,n) value is :",pow().power(x,n))

# def takeInput():
#   cases = int(input())
#   while cases > 0:
#     size = int(input())
#     arr = list(map(int, input().split()))
#   # num = int(input())
#     print(mean(arr))
#     cases -=1

#code
# import math
549755813888
# print(round(math.log(0,2),1).is_integer())

def rotation(a,r):
    i = 0
    while i > int(r):
        rem = a.pop(0)
        a.append(rem)
        i += 1
    return " ".join(map(str, a))
    
def missing(arr,n):
  return sum(range(n+1)) - sum(arr)



def power(num):
    if(num > 0):
      # return "YES" if round(math.log(num, 2),2).is_integer() else "NO"
      pass


def majority(arr,n):
    for i in range(n):
        if(arr.count(i) > n//2):
            return i
    return -1


    
# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     print(majority(arr, n))

def subArraySum(arr, n, sum): 
    for i in range(n): 
        curr_sum = arr[i] 
        j = i + 1
        while j <= n: 
            if curr_sum == sum: 
               print(i+1, (j-1)+1) 
               return ""
                  
            if curr_sum > sum or j == n: 
                break
              
            curr_sum = curr_sum + arr[j] 
            j += 1
    return 0


def series(n):
  # x = [1,2,3]
  i=1
  sums = 0
  while i<=n:
    val = i*(i+1)/2
    sums+=val
    i+=1
  return int(sums)

cases = int(input())
while cases > 0:
    # size, sums= input().split()
    # arr = list(map(int, input().split()))
    num = int(input())
    print(series(num))
    cases -=1


def rotation(a,r):
    i = 0
    while i > int(r):
        rem = a.pop(0)
        a.append(rem)
        i += 1
    return " ".join(map(str, a))
    
def missing(arr,n):
  return sum(range(n+1)) - sum(arr)


def majority(arr,n):
    for i in range(n):
        if(arr.count(i) > n//2):
            return i
    return -1

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
  i=1
  sums = 0
  while i<=n:
    val = i*(i+1)/2
    sums+=val
    i+=1
  return int(sums)

def firstAlphabet(S):
  lis = S.split()
  for i in lis:
    print(i[0], end ="")
  return ""

def setBits(N):
  val = bin(N)
  return val.count("1")

def lexically(n,s):
  minVal = n[0]
  maxVal = n[0]
  for i in range(1,s):
    if(n[i]<minVal):
      minVal =n[i]
    elif(n[i]>maxVal):
      maxVal=n[i]
  return " ".join([minVal,maxVal])

  # or
  minVal = min(n)
  maxVal = max(n)

def removeDuplicates(s):
  result = []
  for i in range(len(s)):
    if(s[i] not in result):
      result.append(s[i])
  return "".join(result)

def moveZeroes(nums):
  x = nums.count(0)
  for i in range(x):
    nums.remove(0)
    nums.append(0)
  return nums

def longestSub(a):
    count=0
    maxCount = 0
    for i in a:
        if(int(i)>0):
            count+=1
        else:
            count=0
        maxCount = max(maxCount,count)
    return maxCount

def leader(s,arr):
  for i in range(s):
    for j in range(i+1,s):
      if(arr[i]<arr[j]):
        break
    if(j==s-1):
      print(arr[i], end=" ")

def printLeaders(arr,size): 
    for i in range(0, size):  
        for j in range(i+1, size):  
            if arr[i]<arr[j]:  
                break
        if j == size-1: # If loop didn't break  
            print(arr[i], end=" ")  
  

def remove(st):
  vowel = ["a","e","i","o","u"]
  ans =[]
  for i in st:
    if(i not in vowel):
      ans.append(i)
  return "".join(ans)

def sorted(unsorted_list,sorted_list):
  while unsorted_list:
      minimum = unsorted_list[0]
      for item in unsorted_list:
          if item < minimum:
              minimum = item
              print(minimum)
      sorted_list.append(minimum)
      unsorted_list.remove(minimum)

def countPrime(n):
  countN=0
  countP=0
  for i in range(2,n):
    for j in range(1,n):
      if(i%j==0):
        countN+=1
    if(countN==2):
      countP+=1
    countN=0
  return countP
    
      
# cases = int(input())
# while cases > 0:
#     size= int(input())
#     arr = list(map(int, input().split()))
#     # num = int(input())
#     printLeaders(arr,size)
#     cases -=1

# print(countPrime(10))


def calc(m):
  sums=0
  for i in range(1,m+1):
    num = i*10
    sums+=num
  return sums

# print(calc(12))

# 7
# 10 7 9 3 2 1 15
# GUVI
def smallNum():
  size = int(input())
  arr = list(map(int,input().split()))
  result=[]
  for i in range(size):
    j=i+1
    while j<size:
      if(arr[j]<arr[i]):
        result.append(arr[j])
        break
      else:
        j+=1
  add = len(result)
  while add<size:
    result.append(-1) 
    add+=1 
  print(" ".join(str(r) for r in result))

def beautiful(a):
  sum=0
  for i in a:
    sum+=i
  if(i%2==0 and i%3==0 and i%5==0):
    return 1
  else:
    return 0
# 5 25 35 -5 30
# size = int(input())
# arr = list(map(int,input().split()))
# print(beautiful(arr))

x =[10,30,80,90,4,3,0]
v=sorted(x)
print(v)
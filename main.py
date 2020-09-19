
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



cases = int(input())
while cases > 0:
    size= int(input())
    arr = list(map(str, input().split()))
    # num = int(input())
    print(longestSub(arr))
    cases -=1
def remove(st):
  vowel = ["a","e","i","o","u"]
  ans =[]
  for i in st:
    if(i not in vowel):
      ans.append(i)
  return "".join(ans)

print(remove("abcdefghiiixcvuu")) 
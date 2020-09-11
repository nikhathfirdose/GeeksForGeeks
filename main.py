# N = list(map(int, input("Enter array: ").split(",")))

def solve(n):
  arr = []
  for i in range(1,n+1):
    if(i%3==0 and i%5==0):
      arr.append("FizzBuzz")
    elif(i%3==0):
      arr.append("Fizz")
    elif(i%5==0):
      arr.append("Buzz")
    else:
      arr.append(i)
  ans = list(map(str,arr))
  return ans

# print(solve(N))

def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
  
def maxVal(arr):
  # length = len(arr)
  max_count = 0
  for num in arr:
    count = arr.count(num)
    prev = max_count
    max_count = max(max_count,count)
    
    if(max_count > prev):
      value = num
  return value

# print(maxVal(N))
def majorityElement(nums):
  dic = {}
  for num in nums:
    if num not in dic:
      dic[num] = 1
    if dic[num] > len(nums)//2:
      print(dic)
      return num
    else:
      dic[num] += 1 

# print(majorityElement(N))  

def calc(arrayVal):
  product =1
  for val in arrayVal:
    product *= val
  return product



def composite(num):
    dic = {}
    # arr =[]
    for i in range(2,num+1):
      dic[i] = 1
      for j in range(2,num+1):
            if(i%j==0):
                dic[i] +=1
    for k, v in dic.items():
      if(v>2):
        print(k, end = " ")
    
        
def mean(arrVal):
  sum = 0
  for val in arrVal:
    sum+=val
    result = sum/len(arrVal)
  return int(result)


def takeInput():
  cases = int(input())
  while cases > 0:
    size = int(input())
    arr = list(map(int, input().split()))
  # num = int(input())
    print(mean(arr))
    cases -=1
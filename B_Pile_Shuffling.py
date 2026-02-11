test_case = int(input())
for i in range(test_case):
     n = int(input())
     min_operation = 0
     for i in range(n):
          a, b , c , d= map(int, input().split())
          # to remove b ones, first we have to remove the zeros
          if (b > d):
               min_operation += a + (b-d)
          elif (a > c):
               min_operation += (a-c)
     print(min_operation)

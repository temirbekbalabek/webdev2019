def lone_sum(a, b, c):
  sum = a + b + c
  if a == b:
    sum = sum - a - b
  if a == c:
    sum = sum - a - c
  if b == c:
    sum = sum - b - c
  if (( a == b ) and (b==c)):
    sum = 0
  return sum;

import sys

def main(arr): 
  print(arr)
  left_maxes = []
  right_maxes = []
  curr_max = 0
  for num in arr:
    if (num > curr_max):
      curr_max = num
    left_maxes.append(curr_max)
  arr.reverse()
  curr_max = 0
  print(left_maxes)
  for num in arr:
    if (num > curr_max):
      curr_max = num
    right_maxes.append(curr_max)
  right_maxes.reverse()
  print(right_maxes)
  arr.reverse()

  total = 0
  for i, floor in enumerate(arr):
   
    left = left_maxes[i]
    right = right_maxes[i]
    print("left", left)
    print("right", right)
    print("min", min(left, right))
    print(i, floor)
    minimum = min(left, right)
    total += (minimum - floor)
    print("- - - - -")
  return total


if (__name__) == '__main__':
    arr = [ int(a) for a in sys.argv[1].split(',') ]
    max_area = main(arr)
    print("max area: %s" % max_area)
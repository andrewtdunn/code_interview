import sys


def process_string(input_string):
  output_arr = []
  for letter in input_string:
    if letter == '#':
      if len(output_arr) > 0:
        output_arr.pop()
    else:
      output_arr.append(letter)
  return ("").join(output_arr)

def main(string1, string2):
  output1 = process_string(string1)
  output2 = process_string(string2)
  print("%s : '%s'" % (string1, output1))
  print("%s : '%s'" % (string2, output2))
  return output1 == output2


if (__name__) == '__main__':
    string1 = sys.argv[1] 
    string2 = sys.argv[2] 
    strings_equal = main(string1, string2)
    print("compare %s and %s: %s" % (string1, string2, strings_equal))

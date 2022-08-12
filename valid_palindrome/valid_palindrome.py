import sys
import re

def strip_punctation(input_string):
  split = re.split(' |,|:', input_string)
  # print("split: %s" % input_string)
  return ("".join(split)).lower()



def test_palindrome(input_string):
  if not len(input_string):
    return True
  print("Testing: %s" % input_string)
  reverse = input_string[::-1]

  # print("reverse: %s " % strip_punctation(reverse))

  # print("original_input: %s " % strip_punctation(input_string))

  return strip_punctation(reverse) == strip_punctation(input_string)


def main(input_string):
  is_palindrome = test_palindrome(input_string)

  print("Is '%s' a palindrome? %s"  % (input_string, is_palindrome))

  return is_palindrome


if (__name__) == '__main__':
  input_string = sys.argv[1]

  main(input_string)
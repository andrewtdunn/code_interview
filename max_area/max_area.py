import sys 

def find_area(left_index, right_index, left_value, right_value):
    return min(left_value, right_value) * (right_index - left_index)

def main(arr): 
    # print("input {}: ".format(arr))
    curr_left_index = 0
    curr_right_index = len(arr) - 1
    max_area = 0

    while curr_left_index != curr_right_index:
        test_area = find_area(curr_left_index, curr_right_index, arr[curr_left_index], arr[curr_right_index])
        max_area = max(test_area, max_area)

        if arr[curr_right_index] < arr[curr_left_index]:
            curr_right_index -= 1
        else: 
            curr_left_index += 1
    return max_area

      

if (__name__) == '__main__':
    arr = [ int(a) for a in sys.argv[1].split(',') ]
    max_area = main(arr)
    print("max area: %s" % max_area)
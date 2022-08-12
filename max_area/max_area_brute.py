import sys 

def main(arr): 
    max_area = 0
    for (i, a) in enumerate(arr):
        for (j, b) in enumerate(arr[i + 1:]):
            second_pointer_index = j + i + 1
            challenger = min(a,b) * second_pointer_index
            max_area = max(challenger, max_area)
    return max_area

if (__name__) == '__main__':
    arr = [ int(a) for a in sys.argv[1].split(',') ]
    max_area = main(arr)
    print("max area: %s" % max_area)
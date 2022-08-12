import sys 

def main(arr, ntf): 
    nums = {}
    for i, num in enumerate(arr):
        target = ntf - num
        if target in nums:
            return [nums[target], i]
        else:
            nums[num] = i
    return None

if (__name__) == '__main__':
    arr = [ int(a) for a in sys.argv[1].split(',') ]
    ntf = int(sys.argv[2])
    indexes = main(arr, ntf)
    print("match found at %s" % indexes)
'''
Move zeros to end.

i/p: 8, 5, 0, 10, 0, 20
o/p: 8, 5, 10, 20, 0, 0

i/p: 0, 0, 0, 0, 10, 0
o/p: 10, 0, 0, 0, 0, 0

i/p: 10, 20
o/p: 10, 20

'''

def zeros_to_end(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[k]
            arr[k] = temp
            k += 1



if __name__ == "__main__":
    items = [10, 10, 0, 20, 0, 30, 0, 0, 0] 
    # items = [0, 20, 0]
    print(items)
    zeros_to_end(items)
    print(items)
    # print(list(res))


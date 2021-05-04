"""
#Get the averages of these numbers

Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and his follower, if there is one.

Example:

Input:  [ 1, 3, 5, 1, -10]
Output:  [ 2, 4, 3, -4.5]

If the array has 0 or 1 values or is null, your method should return an empty array.

Have fun coding it and please don't forget to vote and rank this kata! :-)

def averages(arr):
    return [(arr[x]+arr[x+1])/2 for x in range(len(arr or [])-1)]

"""
def averages(arr):
    if type(arr) != list :return []
    if arr == [] : return []
    res = []
    for i in range(len(arr)-1):
        res.append( (arr[i] + arr[i+1])/2)

    return res

    

if __name__ == "__main__":
    print(averages([ 1, 3, 5, 1, -10]))
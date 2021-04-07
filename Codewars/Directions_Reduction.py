def dirReduc(arr):
    d = [["NORTH", "SOUTH"], ["SOUTH", "NORTH"],
         ["EAST", "WEST"], ["WEST", "EAST"]]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j:j + 2] in d:
                del arr[j:j + 2]
        if arr[i:i + 2] in d:
            del arr[i:i + 2]
    return arr

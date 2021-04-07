def solution(s):
    s = list(s)
    my_list = []
    while len(s):
        if len(s) == 1:
            my_list.append(s.pop(0) + '_')
            return my_list
        my_list.append(s.pop(0) + s.pop(0))
    return my_list


print(solution(input()))

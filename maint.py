from pprint import pprint
import math
import numpy as np

def set_many_list(lst_points):
    lst = [_ for _ in lst_points]
    dct = {}
    answer = []
    # print(lst)
    while lst_points:
        # print(lst_points)
        lst_points = [_ for _ in lst]
        # print(lst_points)
        for i in lst_points:
            # print(lst_points)
            # print(i)

            if i[0] not in dct.keys() and i[1] not in dct.values():
                dct[i[0]] = i[1]
                del lst[lst.index((i[0], i[1]))]
            else:
                # print('break')
                break

        answer.append([(_, dct[_]) for _ in dct.keys()])
        dct.clear()
    return answer

def set_list_x_y(lst):
    x_lst = []
    y_lst = []
    for elem in lst:
        print(elem)
        for e_ in elem:
            for e in e_:
                print(e)
                x_lst.append(e[0])
                y_lst.append(-e[1])
    print('---')
    pprint((np.asarray(x_lst), np.asarray(y_lst)))
    print('---')
    return (np.asarray(x_lst), np.asarray(y_lst))


abc = [(_, int(math.sin(_/10)* 100)) for _ in range(-156, 360)]
# pprint(abc)

# print('-------------------')
# pprint(set_many_list(abc))
answer = set_many_list(abc)

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
    x_lst_ = []
    y_lst_ = []
    for elem in lst:
        # print(elem)
        for e_ in elem:
            # print(e_)
            for e in e_:
                # print(e)
                # print(e)
                x_lst.append(e[0])
                y_lst.append(-e[1])
            x_lst_.append(x_lst)
            y_lst_.append(y_lst)
            # print('xxxx', x_lst, y_lst)
            x_lst = []
            y_lst = []
        # print(x_lst, y_lst)
    # print('---')
    # pprint((np.asarray(x_lst), np.asarray(y_lst)))
    # print(x_lst_)
    # print(y_lst_)
    # print('------------------------')
    return (x_lst_, y_lst_)


abc = [(_, int(math.sin(_/10)* 100)) for _ in range(-156, 360)]
# pprint(abc)

# print('-------------------')
# pprint(set_many_list(abc))
answer = set_many_list(abc)

from pprint import pprint
import math
import numpy as np

def set_many_list(lst_points):
    lst = list([_ for _ in lst_points])
    print(lst)
    # print(len(lst_points), len(lst))
    dct_up = {}
    dct_down = {}
    dct_up_y = {}
    dct_down_y = {}

    dct_up_ = {}
    dct_down_ = {}
    dct_up_y_ = {}
    dct_down_y_ = {}
    answer = []
    # print(type(lst))
    while lst_points:
        # print(len(lst_points))
        # print(lst_points)
        lst_points = [_ for _ in lst]
        UP, DOWN = True, True
        UP_Y, DOWN_Y = True, True
        UP_, DOWN_ = True, True
        UP_Y_, DOWN_Y_ = True, True
        # print(lst_points)
        for i in lst_points:
            DEL = False
            # print(lst_points)
            # print(i)
            try:
                if UP and i[0] >= max(dct_up.keys()) and i[1] >= max(dct_up.keys()):
                    dct_up[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    UP = False

                if DOWN and i[0] <= min(dct_up.keys()) and i[1] <= min(dct_up.keys()):
                    dct_down[i[0]] = i[1]
                    DEL = True

                else:
                    # print('break')
                    DOWN = False

                if UP_Y and i[1] >= max(dct_up_y.keys()) and i[0] >= max(dct_up_y.keys()):
                    dct_up_y[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    UP_Y = False
                if DOWN_Y and i[1] <= max(dct_down_y.keys()) and i[0] <= max(dct_down_y.keys()):
                    dct_down_y[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    DOWN_Y = False




                if UP_ and i[0] >= max(dct_up_.keys()) and i[1] <= max(dct_up_.keys()):
                    dct_up_[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    UP_ = False

                if DOWN_ and i[0] <= max(dct_down_.keys()) and i[1] >= max(dct_down_.keys()):
                    dct_down_[i[0]] = i[1]
                    DOWN_ = True
                else:
                    # print('break')
                    UP = False

                if UP_Y_ and i[0] >= max(dct_up_y_.keys()) and i[1] <= max(dct_up_y_.keys()):
                    dct_up_y_[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    UP_Y_ = False

                if DOWN_Y_ and i[0] <= max(dct_down_y_.keys()) and i[1] >= max(dct_down_y_.keys()):
                    dct_down_y_[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    DOWN_Y_ = False
            except ValueError:
                dct_up[i[0]] = i[1]
                dct_down[i[0]] = i[1]
                dct_up_y[i[0]] = i[1]
                dct_down_y[i[0]] = i[1]
                dct_up_[i[0]] = i[1]
                dct_down_[i[0]] = i[1]
                dct_up_y_[i[0]] = i[1]
                dct_down_y_[i[0]] = i[1]
                DEL = True

            if DEL:
                del lst[lst.index(i)]
            if not UP and not DOWN:
                break
        list_lst = [[(_, dct_up[_]) for _ in dct_up.keys()], [(_, dct_down[_]) for _ in dct_down.keys()],
                    [(_, dct_up_y[_]) for _ in dct_up_y.keys()], [(_, dct_down_y[_]) for _ in dct_down_y.keys()],
                    [(_, dct_up_[_]) for _ in dct_up_.keys()], [(_, dct_down_[_]) for _ in dct_down_.keys()],
                    [(_, dct_up_y_[_]) for _ in dct_up_y_.keys()], [(_, dct_down_y_[_]) for _ in dct_down_y_.keys()]]
        a = sorted(list_lst, key=lambda x: len(x), reverse=True)
        # print([len(a[i]) for i in range(len(a))])
        answer.append(a[0])
        # if len(dct_up) > len(dct_down):
        #     answer.append([(_, dct_up[_]) for _ in dct_up.keys()])
        # else:
        #     answer.append([(_, dct_down[_]) for _ in dct_down.keys()])

        dct_up.clear()
        dct_down.clear()
        dct_up_y.clear()
        dct_down_y.clear()
    print(answer)
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


# abc = [(_, int(math.sin(_/10)* 100)) for _ in range(-156, 360)]
# # pprint(abc)
#
# # print('-------------------')
# # pprint(set_many_list(abc))
# answer = set_many_list(abc)

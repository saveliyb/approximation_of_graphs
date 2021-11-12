def set_many_list(lst_points):
    lst = list([_ for _ in lst_points])
    print(lst)
    # print(len(lst_points), len(lst))
    dct_up = {}
    dct_down = {}
    dct_up_y = {}
    dct_down_y = {}
    answer = []
    # print(type(lst))
    while lst_points:
        # print(len(lst_points))
        # print(lst_points)
        lst_points = [_ for _ in lst]
        UP, DOWN = True, True
        UP_Y, DOWN_Y = True, True
        # print(lst_points)
        for i in lst_points:
            DEL = False
            # print(lst_points)
            # print(i)
            try:
                if UP and i[0] >= max(dct_up.keys()):
                    dct_up[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    UP = False

                if DOWN and i[0] <= min(dct_up.keys()):
                    dct_down[i[0]] = i[1]
                    DEL = True

                else:
                    # print('break')
                    DOWN = False

                if UP_Y and i[1] >= max(dct_up_y.keys()):
                    dct_up_y[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    UP_Y = False
                if DOWN_Y and i[1] <= max(dct_down_y.keys()):
                    dct_down_y[i[0]] = i[1]
                    DEL = True
                else:
                    # print('break')
                    DOWN_Y = False
            except ValueError:
                dct_up[i[0]] = i[1]
                dct_down[i[0]] = i[1]
                dct_up_y[i[0]] = i[1]
                dct_down_y[i[0]] = i[1]
                DEL = True

            if DEL:
                del lst[lst.index(i)]
            if not UP and not DOWN:
                break
        list_lst = [[(_, dct_up[_]) for _ in dct_up.keys()], [(_, dct_down[_]) for _ in dct_down.keys()],
                    [(_, dct_up_y[_]) for _ in dct_up_y.keys()], [(_, dct_down_y[_]) for _ in dct_down_y.keys()]]
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


def period(p: int, ten: str, five: str, one: str) -> str:
    if p == 9:
        return one + ten
    elif p >= 5:
        return five + one * (p - 5)
    elif p == 4:
        return one + five
    else:
        return one * p

def roman(num):
    chlist = "VXLCDM"
    rev = [int(ch) for ch in reversed(str(num))]
    chlist = ["I"] + [chlist[i % len(chlist)] + "\u0304" * (i // len(chlist))
                    for i in range(0, len(rev) * 2)]
    return "".join(reversed([period(rev[i], chlist[i * 2 + 2], chlist[i * 2 + 1], chlist[i * 2])
                            for i in range(0, len(rev))]))


# abc = [(_, int(math.sin(_/10)* 100)) for _ in range(-156, 360)]
# # pprint(abc)
#
# # print('-------------------')
# # pprint(set_many_list(abc))
# answer = set_many_list(abc)

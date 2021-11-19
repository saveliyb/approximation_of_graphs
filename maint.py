def set_many_list(lst_points):
    '''splits the list of points into a list of several patents'''
    lst = list([_ for _ in lst_points])
    dct_up = {}
    dct_down = {}
    dct_up_y = {}
    dct_down_y = {}
    answer = []
    while lst_points:
        lst_points = [_ for _ in lst]
        UP, DOWN = True, True
        UP_Y, DOWN_Y = True, True
        for i in lst_points:
            DEL = False
            try:
                if UP and i[0] >= max(dct_up.keys()):
                    dct_up[i[0]] = i[1]
                    DEL = True
                else:
                    UP = False

                if DOWN and i[0] <= min(dct_up.keys()):
                    dct_down[i[0]] = i[1]
                    DEL = True

                else:
                    DOWN = False

                if UP_Y and i[1] >= max(dct_up_y.keys()):
                    dct_up_y[i[0]] = i[1]
                    DEL = True
                else:
                    UP_Y = False
                if DOWN_Y and i[1] <= max(dct_down_y.keys()):
                    dct_down_y[i[0]] = i[1]
                    DEL = True
                else:
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
        answer.append(a[0])

        dct_up.clear()
        dct_down.clear()
        dct_up_y.clear()
        dct_down_y.clear()
    return answer


def set_list_x_y(lst):
    '''generates two lists of x and y from a list of the format (x, y)'''
    x_belong = []
    x_lst = []
    y_lst = []
    x_lst_ = []
    y_lst_ = []
    for elem in lst:

        for e_ in elem:

            for e in e_:

                x_lst.append(e[0])
                y_lst.append(-e[1])
            x_lst_.append(x_lst)
            y_lst_.append(y_lst)

            x_lst = []
            y_lst = []
    for elem in x_lst_:
        print(elem)
        if elem:
            x_belong.append((min(elem), max(elem)))

    return (x_lst_, y_lst_, x_belong)


def period(p, ten, five, one):
    '''function for the offset in Roman numbers'''
    if p == 9:
        return one + ten
    elif p >= 5:
        return five + one * (p - 5)
    elif p == 4:
        return one + five
    else:
        return one * p

def roman(num):
    '''function for converting Arabic numerals to Roman numerals'''
    chlist = "VXLCDM"
    rev = [int(ch) for ch in reversed(str(num))]
    chlist = ["I"] + [chlist[i % len(chlist)] + "\u0304" * (i // len(chlist))
                    for i in range(0, len(rev) * 2)]
    return "".join(reversed([period(rev[i], chlist[i * 2 + 2], chlist[i * 2 + 1], chlist[i * 2])
                            for i in range(0, len(rev))]))


def plus_or_minus(number):
    '''function for selecting a sign to be substituted into the final formula for output'''
    if float(number) > 0:
        return ' + '
    else:
        return ' - '

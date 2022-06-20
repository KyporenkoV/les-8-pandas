import pandas
import numpy


def raw_data_all_in_one():
    file = pandas.read_csv('data.csv', sep=';')

    a = file['ITT 1'].value_counts(sort=True)
    b = file['ITT2'].value_counts(sort=True)
    c = file['ITT3'].value_counts(sort=True)
    d = file['ITT4'].value_counts(sort=True)
    e = file['ITT5'].value_counts(sort=True)

    res = {}
    for x in [a, b, c, d, e]:
        for y in x:
            if y in res:
                res.update({y: res[y] + x[y]})
            else:
                res.update(x)

    return pandas.Series(res)


def sorted_data(data):
    return pandas.Series(data).sort_values(ascending=False)[0]


def get_pref_color(data):
    data = dict(data)
    res1 = {}
    res2 = {}

    for x in data:
        if x.__divmod__(2)[1] == 0:
            res2.update({x: data[x]})
        else:
            res1.update({x: data[x]})

    red, black = 0, 0

    for x in res1:
        black += res1[x]

    for y in res2:
        if y == 0:
            continue
        else:
            red += res2[y]

    if red > black:
        res_color = "red"
    elif red < black:
        res_color = "black"
    else:
        res_color = 'equal'

    return res_color


def zero(data):
    return dict(data)[0]


def total_spin(data):
    s = data.value_counts(normalize=True)
    return s


raw_data = raw_data_all_in_one()
print('number wich gets most often')
print(sorted_data(raw_data))
print('*' * 20, '\n')

print('Most often color (paired - black, not paired red)')
print(get_pref_color(raw_data))
print('*' * 20, '\n')

print('Print %  when 0 was swown')
print(zero(raw_data))
print(total_spin(raw_data))
print('*' * 20, '\n')

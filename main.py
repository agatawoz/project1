from datetime import datetime

f1 = open("wydatki.txt", "a+")
f2 = open("limit.txt", "a+")


def add():
    k = input("kwota: ")
    d = input("data: ")
    o = input("opis: ")
    all = f"kwota: {k} zl , data: {d}, opis: {o} \n"
    f1.write(all)


def set_limit():
    lim = input("Ustaw nowy limit: ")
    limit = lim + "\n"
    f2.write(limit)


def check_limit():
    print()

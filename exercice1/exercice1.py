def join(list, seperator):
    res = ""
    for s in list:
        if res != "":
            res = f"{res}{seperator}{s}"
        else:
            res = f"{s}"
    return res


def average(list):
    moyenne = 0
    for n in list:
        moyenne += n
    return moyenne / len(list)

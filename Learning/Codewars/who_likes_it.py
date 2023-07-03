def likes(names):
    name = ""
    if not len(names):
        name = 'no one likes this'
    elif len(names) == 1:
        name = str(names[0] + ' likes this')
    elif len(names) == 2:
        name = names[0] + ' and ' + names[1] + ' like this'
    elif len(names) == 3:
        name = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        name = names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others like this'
    print(name)


likes(['Max', 'John', 'Mark', 'Tom'])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
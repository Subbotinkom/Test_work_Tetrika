# Сложность в худшем случае линейная, в лучшем O(log n)
# Но лучше конечно использовать array.find('0'), как наиболее оптимизированный метод


def task(array):
    pos = 0
    while array[int(len(array) / 2)] != '0':
        pos += int(len(array) / 2)
        array = array[int(len(array) / 2):]

    for i, el in enumerate(array):
        if el == '0':
            pos += i
            break
    return pos


s = "111111111111111111111111100000000"
print(task("111111111111111111111111100000000"))

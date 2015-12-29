a = [1, 2, 3]
b = [3, 2, 1]
c = [1, 3, 2]
d = [1, 2, 3, 4]
e = [1, 2, 3]



def compare_list(list1, list2):
    if len(list1) != len(list2):
        return False
    return all([0 for num1, num2 in zip(list1, list2) if num1 != num2])

def compare_list_verbose(list1, list2):
    if len(list1) != len(list2):
        return False

    for num1, num2 in zip(list1, list2):
        if num1 != num2:
            return False
    return True


def main():
    print compare_list(a, b)
    print compare_list(a, c)
    print compare_list(a, d)
    print compare_list(a, e)
    print
    print compare_list_verbose(a, b)
    print compare_list_verbose(a, c)
    print compare_list_verbose(a, d)
    print compare_list_verbose(a, e)
    print
    print a == b
    print a == c
    print a == d
    print a == e

if __name__ == '__main__':
    main()



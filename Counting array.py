def counting_array(count, lst, element):
    add = []
    for i in lst:
        if i >= 2 * element:
            add.append(i)
        else:
            print("Sorry")
        print(add)

count = 3
lst = [4, 6, 7]
element = 3

counting_array(count, lst, element)

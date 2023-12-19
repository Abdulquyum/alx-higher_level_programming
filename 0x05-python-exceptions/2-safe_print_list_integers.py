#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in my_list:
            lent = 0
            count = 0
            while count <= 1:
                if i.isdigit() = True:
                    print("{:d}".format(i), end='')
                    lent += 1
                else:
                    continue
                count += 1
    except:
        pass

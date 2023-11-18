
def search(list_obj, item):
    if list_obj is None:
        return -1
    if list_obj.value == item:
        return 1

    else:
        res = search(list_obj.next, item)
        # print(f"Element {list_obj.value}, res= {res}")
        if res == -1:
            return -1
        return res + 1


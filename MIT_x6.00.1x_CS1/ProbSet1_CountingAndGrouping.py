# Counting and Grouping --groceries


def item_order(order):
    salad = 0
    hamburger = 0
    water = 0

    begcart = 0
    cart = 0
    while cart > -1:
        cart = order.find(' ', begcart)
        if cart == -1:
            word = order[begcart:]
        else:
            word = order[begcart:cart]
        if word == "salad":
            salad += 1
        if word == "hamburger":
            hamburger += 1
        if word == "water":
            water += 1
        begcart = cart+1
    endorder = "salad:"+str(salad)+" hamburger:"+str(hamburger)+" water:"+str(water)
    return endorder

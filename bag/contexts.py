
def bag_contents(request):

    bag_items = 0
    total = 0
    product_count = 0


    context = {
        'bag_items': bag_items,
        'product_count': product_count
        'total': total
        'delivery':delivery
    }

    return context
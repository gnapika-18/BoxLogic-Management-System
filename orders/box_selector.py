from .models import Box, Order 

def recommend_box(order_id):
    order = Order.objects.get(id=order_id)

    total_weight = 0

    for item in order.items.all():
        total_weight += item.product.weight * item.quantity


    total_length = 0
    max_width = 0
    max_height = 0
    

    for item in order.items.all():
        product = item.product
        total_length += product.length * item.quantity
        max_width = max(max_width, product.width)
        max_height = max(max_height, product.height)

        suitable_boxes = []

    for box in Box.objects.all():
        if (
            box.length >= total_length
            and box.width >= max_width
            and box.height >= max_height
            and box.max_weight >= total_weight
            ):
            suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    recommended_box = min(suitable_boxes, key=lambda box: box.cost)

    return recommended_box
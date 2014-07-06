

def out_of_bounds(rect, map_width, map_height):
    oob_right = rect.right > map_width
    oob_bottom = rect.bottom > map_height
    oob_left = rect.left < 0
    oob_top = rect.top < 0
    if oob_right:
        rect.right = map_width
    if oob_bottom:
        rect.bottom = map_height
    if oob_left:
        rect.left = 0
    if oob_top:
        rect.top = 0
    return any((oob_right, oob_bottom, oob_left, oob_top))

def construct(max_height, height, width):
        if max_height == 0:
            return []
        else:
            if height > 0:
                return ['x' * width] + construct(max_height - 1, height - 1, width)
            else:
                return [' ' * width] + construct(max_height - 1, height - 1, width)

def construct_park(max_height, width, height):
        if max_height == 0:
            return []
        else:
            if height > 0:
                if height > 3:
                    height -= 1
                    middle = width // 2
                    return [" " * middle + "|" + " " * middle] + \
                    construct_park(max_height - 1, width, height)
                else:
                    if height == 3:
                        middle = (width - 5) // 2
                        return [" " * middle + "*****" + " " * middle] \
                        + construct_park(max_height - 1, width, height - 1)
                    elif height == 2:
                        middle = (width - 3) // 2
                        return [' ' * middle + "***" + " " * middle] + \
                        construct_park(max_height - 1, width, height - 1)
                    elif height == 1:
                        middle = width // 2
                        return [' ' * middle + "*" + " " * middle] + \
                        construct_park(max_height - 1, width, height - 1)
            else:
                return [' ' * width] + construct_park(max_height - 1, width, height - 1)

def construct_lot(max_height, width, trash):
        if max_height == 0:
            return []
        else:
            if max_height > 1:
                return construct_lot(max_height - 1, width, trash) + [' ' * width]
                
            elif max_height == 1:
                full = width // len(trash)
                remainder = width % len(trash)
                
                remaining = trash[0:remainder]
                
                return construct_lot(max_height - 1, width, trash) + [trash * full + remaining]
                    

            
            
print(construct_lot(8, 11, "__~"))
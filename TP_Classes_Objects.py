import math, copy

class Point(object):
    '''Tao 1 class la toa do cac diem trong Oxy'''

def distance_between_point(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    result = math.sqrt(dx**2 + dy**2)
    return result

class Rectangle(object):
    '''Class Rectangle voi attributes: chieu dai, rong, toa do cua 1 trong 4 goc'''

def move_rectangle(rect, dx, dy):
    rect.original.x += dx
    rect.original.y += dy

def move_rectangle_copy(rect, dx, dy):
    rectnew = copy.deepcopy(rect)
    move_rectangle(rectnew, dx, dy)
    return rectnew

def main():
    point1 = Point()
    point1.x, point1.y = 3.0, 5.0

    point2 = Point()
    point2.x, point2.y = 8.0, 2.0

    print 'distance between 2 point = ', distance_between_point(point1, point2)

    rect = Rectangle()
    rect.height = 100.0
    rect.width = 200.0
    rect.original = Point()
    rect.original.x = 10.0
    rect.original.y = 20.0

    distx, disty = 20.0, 10.0

    new = move_rectangle_copy(rect, distx, disty)
    print 'new original coordinate = ', (new.original.x, new.original.y)
    
    move_rectangle(rect, distx, disty)  #func move_copy phai execute trc
    print 'modify original coordinate = ', (rect.original.x, rect.original.y)

    print new is rect, new.original.x is rect.original.x


if __name__ == '__main__':
    main()
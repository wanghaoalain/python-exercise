for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5*x + 3*y+z/3 == 100:
            print('big chicken %d, mid chicken %d, small chicken %d' % (x, y, z))

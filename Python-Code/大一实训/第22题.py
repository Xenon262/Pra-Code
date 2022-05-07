i = 0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
                if (x != y) and (y != z) and (z != x):
                    i += 1
                    if i % 3:
                        print("%d%d%d" % (x, y, z), end=" 、")
                    else:
                        print("%d%d%d" % (x, y, z))
print("一共有{}个".format(i))
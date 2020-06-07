# Line Clipping Using CyrusBeck Algorithm

import PIL.ImageDraw as ID, PIL.Image as Image
import numpy as np


def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def cbclipLine(x1, y1, x2, y2):
    normal = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(0, n):
        normal[i][1] = vertices[(i + 1) % n][0] - vertices[i][0]
        normal[i][0] = vertices[i][1] - vertices[(i + 1) % n][1]

    dx = x2 - x1
    dy = y2 - y1
    dp1e = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(0, n):
        dp1e[i][0] = vertices[i][0] - x1
        dp1e[i][1] = vertices[i][1] - y1

    numerator = [0, 0, 0, 0, 0, 0]
    denominator = [0, 0, 0, 0, 0, 0]
    for i in range(0, n):
        numerator[i] = dot(normal[i][0], normal[i][1], dp1e[i][0], dp1e[i][1])
        denominator[i] = dot(normal[i][0], normal[i][1], dx, dy)

    t = [0, 0, 0, 0, 0, 0]
    te = np.array([0])
    tl = np.array([1])
    for i in range(0, n):
        t[i] = float(numerator[i]) / float(denominator[i])
        if denominator[i] > 0:
            te = np.append(te, t[i])
        else:
            tl = np.append(tl, t[i])

    temp0 = np.amax(te)
    temp1 = np.amin(tl)
    if temp0 > temp1:
        return

    NewX1 = float(x1) + float(dx) * float(temp0)
    NewY1 = float(y1) + float(dy) * float(temp0)
    NewX2 = float(x1) + float(dx) * float(temp1)
    NewY2 = float(y1) + float(dy) * float(temp1)
    print('New Point 1: (', NewX1, ', ', NewY1, ')')
    print('New Point 2: (', NewX2, ', ', NewY2, ')')
    draw2.line((NewX1, NewY1, NewX2, NewY2), fill=(0, 255, 0))


def clip(x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), fill=(0, 255, 0))
    cbclipLine(x1, y1, x2, y2)


if __name__ == '__main__':
    im = Image.new("RGB", (640, 480))
    im1 = Image.new("RGB", (640, 480))
    draw = ID.Draw(im)
    draw2 = ID.Draw(im1)
    draw.polygon((200, 50, 250, 100, 200, 150, 100, 150, 50, 100, 100, 50), outline=255)
    draw2.polygon((200, 50, 250, 100, 200, 150, 100, 150, 50, 100, 100, 50), outline=255)
    vertices = [[200, 50], [250, 100], [200, 150], [100, 150], [50, 100], [100, 50]]
    n = 6
    x1 = 80
    y1 = 30
    x2 = 220
    y2 = 200
    clip(x1, y1, x2, y2)
    im.show()
    im1.show()

import cv2
from PIL import Image
import numpy as np


def find_max_pixel_encoded(img):
    image = cv2.imread(img, 0)
    width, height = int(image.shape[1]), int(image.shape[0])
    total_pixel = width*height
    total_vals = int(total_pixel*3/9)
    return total_vals


def resize_img(img, width, height, ip=cv2.INTER_CUBIC):
    image = cv2.imread(img, 1)
    r_width = width
    r_height = height
    resized_dimension = (r_width, r_height)
    resized = cv2.resize(image, resized_dimension, interpolation=ip)
    return resized


def rgb2grey(img):
    image = cv2.imread(img, 0)
    width, height = (int(image.shape[1]), int(image.shape[0]))
    grey_weights = []
    for i in range(height):
        for j in range(width):
            grey_weights.append(image[i][j])
    print(len(grey_weights))
    return [grey_weights, width, height]


def encode_driver(source, img, new_name):
    total_src_val = find_max_pixel_encoded(source)
    weights, w, h = rgb2grey(img)
    print(weights)
    total_img_val = len(weights)
    image = cv2.imread(source, 0)
    width, height = int(image.shape[1]), int(image.shape[0])
    if total_src_val < total_img_val:
        return -1
    else:
        ret = encode(source, weights, width, new_name)
    if ret == 0:
        return 0
    return -1


def encode(source, weights, width, new_name):
    image = Image.open(source, 'r')
    newimg = image.copy()
    (x, y) = (0, 0)
    for pixel in mod_pix(newimg.getdata(), weights):
        newimg.putpixel((x, y), pixel)
        if x == int(width) - 1:
            x = 0
            y += 1
        else:
            x += 1
    newimg.save('Files/'+new_name, str(new_name.split(".")[1].upper()))
    return 0


def gen_binary_data(weights):
    newd = []
    for i in weights:
        newd.append(format(i, '08b'))
    return newd


def mod_pix(pix, data):
    datalist = gen_binary_data(data)
    lendata = len(datalist)
    imdata = iter(pix)
    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                if pix[j] % 2 != 0:
                    pix[j] -= 1
            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                pix[j] -= 1
        if i == lendata - 1:
            if pix[-1] % 2 == 0:
                pix[-1] -= 1
        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def decode(img):
    image = Image.open(img, 'r')
    data = []
    imgdata = iter(image.getdata())
    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'
        data.append(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data


def weight_2_grey(weights, img, width, height):
    # print(weights)
    x = np.array(weights).astype('uint8')
    x = x.reshape(height, width)
    # image = Image.fromarray(x, 'L')
    # image = image.save('dec.png')
    cv2.imwrite('Files/{}.png'.format(str(img)), x)

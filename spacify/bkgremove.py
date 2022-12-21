import cv2
import os
import random
import numpy as np

SPACE_IMGS = 'space imgs'

def dice_roll(SPACE_IMGS):
    print(random.choice(os.listdir(SPACE_IMGS)))
    return random.choice(os.listdir(SPACE_IMGS))


def spacify(image):
    # load image
    img = cv2.imread(image)

    # convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold input image as mask
    mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

    # negate mask
    mask = 255 - mask

    # apply morphology to remove isolated extraneous noise
    # use borderconstant of black since foreground touches the edges
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # anti-alias the mask -- blur then stretch
    # blur alpha channel
    mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)

    # linear stretch so that 127.5 goes to 0, but 255 stays 255
    mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

    # put mask into alpha channel
    result = img.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask


    # save resulting masked image
    filename = image.split('.')[0]
    format = '.' + image.split('.')[1]
    cv2.imwrite(filename + '_tspt' + format, result)

    ##########

    # replace transparent pixels with image pixels
    background = cv2.imread('space imgs' + '/' + dice_roll(SPACE_IMGS), cv2.IMREAD_UNCHANGED)
    foreground = cv2.imread(f'{filename}_tspt{format}', cv2.IMREAD_UNCHANGED)

    # normalize alpha channels from 0-255 to 0-1
    alpha_background = background[:,:,3] / 255.0
    alpha_foreground = foreground[:,:,3] / 255.0

    # set adjusted colors
    for color in range(0, 3):
        background[:,:,color] = alpha_foreground * foreground[:,:,color] + \
                                alpha_background * background[:,:,color] * (1 - alpha_foreground)

    # set adjusted alpha and denormalize back to 0-255
    background[:,:,3] = (1 - (1 - alpha_foreground) * (1 - alpha_background)) * 255
    cv2.imwrite(filename + '_tspt' + format, background)
    ##########

    return f'{filename}_tspt{format}'

if __name__ == '__main__':
    dice_roll(SPACE_IMGS)
    spacify('uploads/left.png')
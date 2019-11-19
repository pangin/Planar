from PIL import Image
from OpenGL.GL import *

def screenshot(image_filename_for_opencv, width, height):
    """
    :param image_filename_for_opencv:
        as variable name says
    :param width:
        width as px
    :param height:
        height as px

    :return:
        image file for opencv
    """
    glReadBuffer(GL_FRONT)
    pixels = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)

    image = Image.fromstring("RGB", (width, height), pixels)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(image_filename_for_opencv)
from PIL import Image
import colorcorrect.algorithm as cca
from colorcorrect.util import from_pil, to_pil


def correctColor(imgPath):
    img = Image.open(imgPath)
    to_pil(cca.stretch(from_pil(img))).save(imgPath)

    return imgPath
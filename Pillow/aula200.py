# pillow : redimensionando imagens
from pathlib import Path

from PIL import Image

ROOT_PATH = Path(__file__).parent
OLD_IMAGE = ROOT_PATH / 'img_original.jpg'
NEW_IMAGE = ROOT_PATH / 'new_img.jpg'

pil_image = Image.open(OLD_IMAGE)
width, height = pil_image.size
# exif = pil_image.info('exif')

new_widht = 640
new_height = round(height * new_widht / width)

new_image = pil_image.resize((new_widht, new_height), Image.LANCZOS)
new_image.save(NEW_IMAGE, optimize=True, quality=70)

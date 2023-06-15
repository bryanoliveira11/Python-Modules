# pypdf2, extrating text and images
from pathlib import Path

from PyPDF2 import PdfReader

ROOT_FOLDER = Path(__file__).parent
PDF_FOLDER = ROOT_FOLDER / 'pdf'
NEW_FOLDER = ROOT_FOLDER / 'new_files'
BACEN_FILE = PDF_FOLDER / 'R20230210.pdf'

NEW_FOLDER.mkdir(exist_ok=True)
reader = PdfReader(BACEN_FILE)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)

page0 = reader.pages[0]

# print(page0.extract_text())
# print(page0.images[0])

# with open(NEW_FOLDER / page0.images[0].name, 'wb') as image:
#     image.write(page0.images[0].data)

i = 0

for image in page0.images:
    with open(NEW_FOLDER / page0.images[i].name, 'wb') as img:
        img.write(page0.images[i].data)
        i += 1

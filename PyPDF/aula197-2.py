# pypdf2, creating pdfs
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

ROOT_FOLDER = Path(__file__).parent
PDF_FOLDER = ROOT_FOLDER / 'pdf'
NEW_FOLDER = ROOT_FOLDER / 'new_files'
BACEN_FILE = PDF_FOLDER / 'R20230210.pdf'

NEW_FOLDER.mkdir(exist_ok=True)
reader = PdfReader(BACEN_FILE)

page0 = reader.pages[0]

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FOLDER / f'PAGE{i}.pdf', 'wb') as pdf:
        writer.add_page(page)
        writer.write(pdf)

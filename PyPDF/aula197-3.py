# pypdf2, pdf merger

from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader

ROOT_FOLDER = Path(__file__).parent
PDF_FOLDER = ROOT_FOLDER / 'pdf'
NEW_FOLDER = ROOT_FOLDER / 'new_files'
BACEN_FILE = PDF_FOLDER / 'R20230210.pdf'

NEW_FOLDER.mkdir(exist_ok=True)
reader = PdfReader(BACEN_FILE)

merger = PdfMerger()

files: list[Path | str] = [NEW_FOLDER / 'PAGE1.pdf', NEW_FOLDER / 'PAGE0.pdf']

for file in files:
    merger.append(file)

with open(NEW_FOLDER / 'MERGED.PDF', 'wb') as merge_pdf:
    merger.write(merge_pdf)

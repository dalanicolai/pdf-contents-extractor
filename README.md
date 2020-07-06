# pdf-contents-extractor 
Extract Table of Contents (TOC) as text from a pdf- or djvu-document (for use in e.g. handyoutliner)

requires:
* for PDF, pytesseract and PyMuPDF (both can be easily installed with pip)
* for DJVU, the ddjvu command available in the path

After installation type in a terminal: extract_contents /path/filename startpage lastpage
(e.g.: `extract_contents example.djvu 3 6`)
where startpage and lastpage are pagenumbers of the content pages.
The script automatically recognizes the format (pdf or djvu)

The default tesseract language is english. Another language(s) can be set with -l flag (e.g.: `-l eng+nld` for english and dutch) but it requires the correct tesseract langpack to be installed.

for extra options and help type: extract_contents -h

There is a cleanup_contents script also which might help cleanup the contents_ocr.txt file, it is handy sometimes but far from perfect. To use it, just run the script in the directory containing the contents_ocr.txt file.

The script creates two files, `contents.txt` and `contents_ocr.txt`. The first file contains contents extracted from the text layer if available (this can be also extracted using handyoutliner (http://handyoutlinerfo.sourceforge.net/)). The second file contains contents extracted using the tesseract OCR engine. The contents can be further edited in a text-editor, although to reduce the work it is recommended to check how well the contents is parsed by [handyoutliner](http://handyoutlinerfo.sourceforge.net/) first. Finally the pdf-file can be added to the PDF/DJVU file with [handyoutliner](http://handyoutlinerfo.sourceforge.net/). 


# pdf-contents-extractor
Extract contents as text from a pdf-document (for use in e.g. handyoutliner)

requires: pytesseract and PyMuPDF (both can be easily installed with pip)

After installation type in a terminal: extract_contents /path/filename startpage lastpage
(e.g.: extract_contents example.pdf 3 6)
where startpage and lastpage are pagenumbers of the content pages.

for extra options and help type: extract_contents --help

The contents can be further edited in a text-editor and added to the pdf-file with handyoutliner (http://handyoutlinerfo.sourceforge.net/)

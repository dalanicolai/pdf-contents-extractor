# pdf-contents-extractor 
Extract contents as text from a pdf- or djvu-document (for use in e.g. handyoutliner)

requires:
* for PDF, pytesseract and PyMuPDF (both can be easily installed with pip)
* for DJVU, the ddjvu command available in the path

After installation type in a terminal: extract_contents /path/filename startpage lastpage
(e.g.: `extract_contents example.djvu 3 6`)
where startpage and lastpage are pagenumbers of the content pages.
The script automatically recognizes the format (pdf or djvu)

The default tesseract language is english. Another language(s) can be set with -l flag (e.g.: `-l eng+nld` for english and dutch) but it requires the correct tesseract langpack to be installed.

for extra options and help type: extract_contents -h

The contents can be further edited in a text-editor and added to the pdf-file with handyoutliner (http://handyoutlinerfo.sourceforge.net/)


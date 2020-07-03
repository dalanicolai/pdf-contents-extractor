import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="document-contents-extractor",
    version="1.1",
    install_requires=[
        "Pillow",
        "PyMuPDF",
        "pytesseract==0.2.7",
    ],
    scripts=['extract_contents'],
    author="Daniel Nicolai",
    author_email="dalanicolai@gmail.com",
    description="A simple script to extract contents section from a PDF or DJVU document",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dalanicolai/pdf-contents-extractor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: POSIX",
    ],
)

#!/usr/bin/env python3
import shutil
import pandas as pd
import convert_stream as cs

from soup_files import File, UserFileSystem, Directory, InputFiles, LibraryDocs
from ocr_stream import RecognizeImage, LibOcr, RecognizePdf, read_image, read_images, read_document
from sheet_stream import TableRow, TableDocuments

DOW = UserFileSystem().userDownloads
OUT = DOW.concat('output', create=True)
out_sheet = OUT.join_file('teste.xlsx')


def test():
    pass


def main():
    test()


main()

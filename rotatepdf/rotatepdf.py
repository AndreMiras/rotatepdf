#!/usr/bin/env python
"""
Rotate pdf pages from command line:
$ ./rotatepdf.py --src src.pdf --dst dst.pdf --rotate-left 1-3
"""

import argparse

from PyPDF2 import PdfFileReader, PdfFileWriter


def hyphen_range(v):
    """
    Returns a range from a given string including lower bounds and
    upper bounds.
    >>> [x for x in hyphen_range("1-3")]
    [1, 2, 3]
    >>> hyphen_range("foobar")
    Traceback (most recent call last):
    ...
    argparse.ArgumentTypeError: String must have 2 fields
    >>> [x for x in hyphen_range("1-1")]
    [1]
    """
    fields = v.split("-")
    if len(fields) != 2:
        raise argparse.ArgumentTypeError("String must have 2 fields")
    else:
        start = int(fields[0])
        stop = int(fields[1])
        page_range = range(start, stop + 1)
        return page_range


def rotate(src_stream, dst_stream, rotate_pages_dict):
    """
    Rotates src_stream to dst_stream given a rotate_pages_dict configuration.
    """
    file_reader = PdfFileReader(src_stream)
    file_writer = PdfFileWriter()
    rotate_left_pages = rotate_pages_dict["rotate_left_pages"]
    rotate_right_pages = rotate_pages_dict["rotate_right_pages"]
    rotate_180_pages = rotate_pages_dict["rotate_180_pages"]
    for zb_page_num in range(file_reader.getNumPages()):
        # zero based page num page num
        page_num = zb_page_num + 1
        if page_num in rotate_180_pages:
            file_writer.addPage(file_reader.getPage(zb_page_num).rotateClockwise(180))
        elif page_num in rotate_left_pages:
            file_writer.addPage(
                file_reader.getPage(zb_page_num).rotateCounterClockwise(90)
            )
        elif page_num in rotate_right_pages:
            file_writer.addPage(file_reader.getPage(zb_page_num).rotateClockwise(90))
        else:
            file_writer.addPage(file_reader.getPage(zb_page_num))
    file_writer.write(dst_stream)


def main():
    parser = argparse.ArgumentParser(description="Rotate pdf pages from command line.")
    parser.add_argument("--src", type=argparse.FileType("rb"), required=True)
    parser.add_argument("--dst", type=argparse.FileType("wb"), required=True)
    help_rotate = "page range to be rotated, e.g 1-3"
    parser.add_argument(
        "--rotate-left", metavar="RANGE", type=hyphen_range, help=help_rotate
    )
    parser.add_argument(
        "--rotate-right", metavar="RANGE", type=hyphen_range, help=help_rotate
    )
    parser.add_argument(
        "--rotate-180", metavar="RANGE", type=hyphen_range, help=help_rotate
    )
    args = parser.parse_args()
    src = args.src
    dst = args.dst
    rotate_left_pages = args.rotate_left or []
    rotate_right_pages = args.rotate_right or []
    rotate_180_pages = args.rotate_180 or []
    rotate_pages_dict = {
        "rotate_left_pages": rotate_left_pages,
        "rotate_right_pages": rotate_right_pages,
        "rotate_180_pages": rotate_180_pages,
    }
    rotate(src, dst, rotate_pages_dict)


if __name__ == "__main__":
    main()

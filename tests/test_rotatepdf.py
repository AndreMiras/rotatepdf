import io

import pytest
from PyPDF2 import PdfReader, PdfWriter

from rotatepdf import rotate


@pytest.fixture
def sample_pdf():
    """Creates an in-memory 3-page PDF."""
    writer = PdfWriter()
    for _ in range(3):
        writer.add_blank_page(width=72, height=72)
    pdf_stream = io.BytesIO()
    writer.write(pdf_stream)
    pdf_stream.seek(0)
    return pdf_stream


def test_rotate_left(sample_pdf):
    output_stream = io.BytesIO()
    rotate(
        sample_pdf,
        output_stream,
        {"rotate_left_pages": [1], "rotate_right_pages": [], "rotate_180_pages": []},
    )
    output_stream.seek(0)
    reader = PdfReader(output_stream)
    page = reader.pages[0]
    assert page.get("/Rotate") == -90


def test_rotate_right(sample_pdf):
    output_stream = io.BytesIO()
    rotate(
        sample_pdf,
        output_stream,
        {"rotate_left_pages": [], "rotate_right_pages": [1], "rotate_180_pages": []},
    )
    output_stream.seek(0)
    reader = PdfReader(output_stream)
    page = reader.pages[0]
    assert page.get("/Rotate") == 90


def test_rotate_180(sample_pdf):
    output_stream = io.BytesIO()
    rotate(
        sample_pdf,
        output_stream,
        {"rotate_left_pages": [], "rotate_right_pages": [], "rotate_180_pages": [1]},
    )
    output_stream.seek(0)
    reader = PdfReader(output_stream)
    page = reader.pages[0]
    assert page.get("/Rotate") == 180

"""Test"""
import pytest
from app.services.number_extractor import NumberExtractor


def test_extract_valid_number():
    extractor = NumberExtractor()
    assert extractor.extract(10) == 10


def test_extract_invalid_number():
    extractor = NumberExtractor()
    with pytest.raises(ValueError):
        extractor.extract(150)


def test_calculate_number_extracted_within_range():
    extractor = NumberExtractor()
    assert extractor.calculate_number_extracted(50) == 50


def test_calculate_number_extracted_minimum():
    extractor = NumberExtractor()
    assert extractor.calculate_number_extracted(1) == 1


def test_calculate_number_extracted_maximum():
    extractor = NumberExtractor()
    assert extractor.calculate_number_extracted(100) == 100


def test_calculate_number_extracted_out_of_range():
    extractor = NumberExtractor()
    with pytest.raises(ValueError):
        extractor.calculate_number_extracted(101)


def test_calculate_number_extracted_negative():
    extractor = NumberExtractor()
    with pytest.raises(ValueError):
        extractor.calculate_number_extracted(-1)

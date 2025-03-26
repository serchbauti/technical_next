import pytest
from app.services.number_extractor import NumberExtractor


def test_extract_valid_number():
    extractor = NumberExtractor()
    assert extractor.extract(10) == 10


def test_extract_invalid_number():
    extractor = NumberExtractor()
    with pytest.raises(ValueError):
        extractor.extract(150)


def test_get_extracted_number():
    extractor = NumberExtractor()
    extractor.extract(25)
    assert extractor.get_extracted() == 25


def test_get_extracted_without_extraction():
    extractor = NumberExtractor()
    with pytest.raises(ValueError):
        extractor.get_extracted()

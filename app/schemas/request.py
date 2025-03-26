"""Schemas"""
from pydantic import BaseModel, Field


class ExtractRequest(BaseModel):
    """Represents a request to extract a number within a specified range.
    Attributes:
        number (int): An integer between 1 and 100, inclusive, to be extracted.
    """
    number: int = Field(
        gt=0,
        lt=101,
        description="Número a extraer (1-100)"
    )

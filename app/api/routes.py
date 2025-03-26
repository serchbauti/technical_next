"""Routes"""
from fastapi import APIRouter, HTTPException
from app.services.number_extractor import NumberExtractor
from app.schemas.request import ExtractRequest

router = APIRouter()


@router.post("/extract/")
def extract_number(request: ExtractRequest):
    """Handles POST requests to extract a number within the range 1-100.
    Args:
        request (ExtractRequest): The request object containing the number to
        extract.
    Returns:
        dict: A message indicating the extracted number.
    Raises:
        HTTPException: If the number is outside the allowed range or if no
        number has been drawn.
    """
    extractor = NumberExtractor()
    try:
        result = extractor.extract(request.number)
        return {"message": f"Se extrajo el número {result}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

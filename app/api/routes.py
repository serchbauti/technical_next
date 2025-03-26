from fastapi import APIRouter, HTTPException
from app.services.number_extractor import NumberExtractor
from app.schemas.request import ExtractRequest

router = APIRouter()


@router.post("/extract/")
def extract_number(request: ExtractRequest):
    extractor = NumberExtractor()
    try:
        result = extractor.extract(request.number)
        return {"message": f"Se extrajo el número {result}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

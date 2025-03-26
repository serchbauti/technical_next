from pydantic import BaseModel, Field


class ExtractRequest(BaseModel):
    number: int = Field(
        gt=0,
        lt=101,
        description="Número a extraer (1-100)"
    )

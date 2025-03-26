from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api.routes import router
from app.services.number_extractor import NumberExtractor

app = FastAPI(title="Number Extractor API", version="1.0")

app.include_router(router, prefix="/api", tags=["Extract"])

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def form_view(request: Request):
    """Handles GET requests to the root URL and renders the
    index.html template.
    Parameters:
        request (Request): The request object containing
        metadata about the request.
    Returns:
        TemplateResponse: A response object that renders the
        specified HTML template.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
def process_extraction(request: Request, number: int = Form(...)):
    """Handles the POST request to extract a number from the
    predefined set.
    Args:
        request (Request): The incoming HTTP request.
        number (int): The number to be extracted, provided via form data.
    Returns:
        TemplateResponse: Renders the 'index.html' template with a success
        message if the number is extracted successfully, or an error message
        if the extraction fails due to an invalid number.
    """
    extractor = NumberExtractor()
    try:
        result = extractor.extract(number)
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "message": f"Se extrajo el número {result}"}
        )
    except ValueError as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": str(e)}
        )

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
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
def process_extraction(request: Request, number: int = Form(...)):
    extractor = NumberExtractor()
    try:
        result = extractor.extract(number)
        return templates.TemplateResponse(
            "index.html", {"request": request, "message": f"Se extrajo el número {result}"})
    except ValueError as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e)})
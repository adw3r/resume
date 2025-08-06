import aiofiles
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from playwright.async_api import async_playwright
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app import config
from app.config import logger

app = FastAPI()
app.mount("/assets", StaticFiles(directory=config.ROOT_FOLDER / "front" / "assets"), name="assets")
templates = Jinja2Templates(directory=config.ROOT_FOLDER / "front")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
url_to_html = str(config.ROOT_FOLDER / "front" / r"Python dev Naidiuk Oleksii.html")
output_path = str(config.ROOT_FOLDER / r"Python dev Naidiuk Oleksii.pdf")


@app.get("/", response_class=HTMLResponse)
async def get_resume(request: Request):
    return templates.TemplateResponse(name="Python dev Naidiuk Oleksii.html", request=request)


@app.get('/resume_in_pdf')
async def get_resume_in_pdf():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(f"http://localhost:{config.PORT}/")
            await page.pdf(path=output_path, format="A4", print_background=True)
            await browser.close()
        return FileResponse(path=output_path, filename='Python dev Naidiuk Oleksii.pdf', media_type='application/pdf')
    except Exception as error:
        logger.exception(error)
        return "Failed"


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=config.HOST, port=config.PORT)

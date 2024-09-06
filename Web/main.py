from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from detect import OCR

app = FastAPI()

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH, 'static/upload')


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template rendering
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "upload": False})

@app.post("/upload", response_class=HTMLResponse)
async def upload_image(request: Request, image_name: UploadFile = File(...)):
    filename = image_name.filename
    path_save = os.path.join(UPLOAD_PATH, filename)
    
    with open(path_save, "wb") as f:
        f.write(image_name.file.read())
    
    file, text = OCR(path_save, filename)
    
    result_html = f"""
    <div id="result">
        <!-- Display results here -->
        
        <table style="border: solid black; width: 100%">
            <tr style="border: solid black">
              <th>CROPPEED LICENCE PLATE IMAGE</th>
              <th>TEXT</th>
            </tr>
            <tr style="border: solid black">
              <td>
                <img class="img-fluid" src="/static/predict/{filename}" alt="" />
              </td>
              <td style="background-color: #c1dce0">
                <h1 class="display-8">{ text }</h1>
              </td>
            </tr>
          </table>
    
    """
    
    return HTMLResponse(content=result_html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

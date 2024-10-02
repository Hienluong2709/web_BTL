from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# Cài đặt thư mục templates cho HTML và static cho CSS/JS
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Mô hình dữ liệu dự đoán rượu vang
class WineInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

# Định nghĩa route cho trang chủ
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Định nghĩa route cho xử lý dự đoán
@app.post("/predict")
async def predict_wine_quality(wine_input: WineInput):
    # Đơn giản hóa bằng cách tính điểm dựa trên nồng độ cồn
    prediction = "Tốt" if wine_input.alcohol > 10 else "Trung bình"
    
    # Trả về kết quả
    return {"prediction": prediction}

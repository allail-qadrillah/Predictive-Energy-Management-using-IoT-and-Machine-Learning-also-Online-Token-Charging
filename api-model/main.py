from fastapi import FastAPI, Query
from api.api import API
from api.util.date_range import Date_Range

api = API()
app = FastAPI()

@app.get("/")
def main():
    return {"status": "success", 
            "message": "Bismillah Juara Indonesian International Internet of Things Competition (I30) 2023"}


@app.get("/predict")
def predict(day: int = Query(..., description="prediksi untuk berapa hari? (kwh)")):
    return {"status": "success",
            "day" : day,
            "range day": Date_Range().get_date_range(day),
            "result" : api.get_prediction(day)
            }


# Menjalankan server dengan uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)

"""
running on terminal:
python -B -m uvicorn main:app --reload
"""

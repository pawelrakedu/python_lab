from fastapi import FastAPI
from PIL import Image, ImageChops
import math
from matplotlib import pyplot as plt
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from datetime import datetime

app = FastAPI()
security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"paweu"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"paweu"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/time")
def read_current_user(username: str = Depends(get_current_username)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return {current_time}


@app.get("/prime/{number}")
async def root(number: int):
    return {"message": is_prime(number)}


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n > 9223372036854775807:
            return {"Liczba poza zakresem"}
        if n < 0:
            return {"Podaj liczbe naturalna"}
        if (n % i) == 0:
            return False
    return True


@app.post("/picture/{image_path:path}")
def take_path(image_path: str):
    return invert_image(image_path)


def invert_image(path):
    img = Image.open(path)
    inv_img = ImageChops.invert(img)
    inv_img.show()

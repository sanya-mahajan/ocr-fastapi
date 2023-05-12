#testin api endpts

import shutil,time
from app.main import app,BASE_DIR,UPLOAD_DIR
from fastapi.testclient import TestClient
from PIL import Image, ImageChops
import io

client = TestClient(app)

def test_home_view():
    response = client.get("/")  #requests.get like
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_echo_upload():
    img_saved_path = BASE_DIR / "images"
    for path in img_saved_path.glob("*"):
        try:
            img = Image.open(path)
        except:
            img = None
        response = client.post("/echo/", files={"file": open(path, 'rb')})
        if img is None:
            assert response.status_code == 400
        else:
            # Returning a valid image
            assert response.status_code == 200
            r_stream = io.BytesIO(response.content)
            echo_img = Image.open(r_stream)
            diff = ImageChops.difference(img, echo_img)
            assert diff.getbbox() is None



time.sleep(3)
shutil.rmtree(UPLOAD_DIR)
# ocr-fastapi

--fastapi + jinja templates


uvicorn app.main:app --reload           (uvi+guni allows async)

--HTMLresponse class
--Response class
--pathlib
--Pytest
--fastapi testclient (like python requests)
--precommit hooks
    -add repo local and to add pytest
    - pre-commit install (for changes)
    -pre-commit run --all-files
    -to disable hooks, delete pre-commit file after cd .git/hooks


![Screenshot from 2023-04-02 11-13-32](https://user-images.githubusercontent.com/88281057/229334062-b0e44838-cb79-4051-a3e5-7844dd0cca49.png)

https://ms-ocr-fastapi.azurewebsites.net/


--add docker (main2)
    --make entrypoint.sh and change gunicorn path (faster than virtualenv)
    --declare runport and bind
    --apt-get python and packages
    --prune files after running to reduce image size
    -- push image to dockerhub

--add debug/.env to main , use BseSettings and lru_cache decorator
-- create dependency on settings in view
--  File and UploadFile class
-- define async function for upload (input bytestr using io)
-- add upload route and use uuid to generate unique filepath
-- add settings dependency in echofile view as well so that it gets value for ECHO_ON
-- add automated test for images

.Headers({'content-type': 'image/png', 'content-length': '61876', 'last-modified': 'Mon, 03 Apr 2023 16:14:42 GMT', 'etag': '5837c4e11ce616aadec140e04b9621a5'})

-- implement pillow for validating image (convert bytestr to img)
-- save image to destination path
-- use imagechops to compare uploaded img vs echo img

-- install pytesseract and make ocr file

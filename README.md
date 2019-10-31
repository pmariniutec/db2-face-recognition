# Face Recognition

### Install
```bash
# BACKEND
# create virtualenv and activate
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# apply migrations to database
python manage.py migrate
```
```bash
# FRONTEND
# install dependencies
npm install
```

### Running

```bash
# local backend on localhost:8000
python manage.py runserver

# local frontend on localhost:8080
npm run serve
```

### Notes
- Create a folder in backend/media/images and include all the pictures for the face recognition app
- `image_recognition.py` is inside backend/image_recognition/

### Project Layout
- django API (backend) + SQLite
- vuejs (frontend)
- `image_recognition.py` (KNN search, RTree, etc)
	- Will be used by the django backend

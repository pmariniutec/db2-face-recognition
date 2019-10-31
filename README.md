# Face Recognition

### Install
```bash
# create virtualenv and activate
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt
```

### Project Layout
- django API (backend)
- vuejs (frontend)
- `face_recognition.py` (KNN search, RTree, etc)
	- Will be used by the django backend

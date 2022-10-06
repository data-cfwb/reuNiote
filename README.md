## reuNiote

Petite application web pour gérer estimer le cout horaire d'une réunion de travail.

- **Demo**

# Run it

First install the dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Then run the app:

```bash
streamlit run app.py
```

# Deploy with Docker

## Build

```bash
docker build --no-cache -f Dockerfile -t app:latest .
```

## Run in daemon mode

```bash
docker run -d -p 8501:8501 app:latest
```

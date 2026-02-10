# Loan Approval Prediction (Streamlit)

This repository contains a Streamlit app (`app.py`) that predicts loan approval using a preserved model and scaler (`model.pickle`, `scaler.pickle`).

Quick start

1. Create a virtual environment and install requirements:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app locally:

```bash
streamlit run app.py
```

Deploy to Streamlit Cloud

- Push this repository to GitHub and then connect it on https://share.streamlit.io — Streamlit will install `requirements.txt` and run `streamlit run app.py` automatically.

Deploy using Docker / Render / Heroku

- Build the provided `Dockerfile` and deploy to your platform of choice. For Heroku, add a `Procfile` and push to a Heroku app.

Notes

- `model.pickle` and `scaler.pickle` are required in the repository root.
- If these files are large, consider using Git LFS.

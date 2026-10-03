# Temperature Converter

A Python + Flask web application that converts temperatures between **Celsius, Fahrenheit, and Kelvin**. The project demonstrates functions, arithmetic operations, input validation, formatted output, automated tests, and deployment on Render.

## Features

- Celsius ↔ Fahrenheit conversion
- Celsius ↔ Kelvin conversion
- Fahrenheit ↔ Kelvin conversion
- Validation for temperatures below absolute zero
- Clean, responsive web interface
- JSON API endpoint for quick testing
- `/health` endpoint for deployment health checks
- Unit tests using Python's built-in `unittest`
- Render deployment configuration included

## Technologies

- Python 3.13
- Flask
- Gunicorn
- HTML5
- CSS3
- Git and GitHub
- Render

## Conversion formulas

- Fahrenheit = (Celsius × 9/5) + 32
- Celsius = (Fahrenheit − 32) × 5/9
- Kelvin = Celsius + 273.15
- Celsius = Kelvin − 273.15
- Kelvin = (Fahrenheit − 32) × 5/9 + 273.15
- Fahrenheit = (Kelvin − 273.15) × 9/5 + 32

## Sample outputs

| Input | Conversion | Output |
|---|---|---:|
| 0 °C | Celsius → Fahrenheit | 32.00 °F |
| 100 °C | Celsius → Fahrenheit | 212.00 °F |
| 0 °C | Celsius → Kelvin | 273.15 K |
| 32 °F | Fahrenheit → Celsius | 0.00 °C |
| 273.15 K | Kelvin → Celsius | 0.00 °C |
| 300 K | Kelvin → Fahrenheit | 80.33 °F |

## Run locally on Windows PowerShell

### 1. Check Python and Git

```powershell
python --version
git --version
```

If `python` is not recognized, install Python and make sure **Add Python to PATH** is enabled.

### 2. Extract the project and enter the folder

```powershell
cd "C:\path\to\temperature_converter_project"
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run tests

```powershell
python -m unittest discover -s tests -v
```

### 6. Start the app

```powershell
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

### 7. Test the API

Open:

`http://127.0.0.1:5000/api/convert?value=100&from=C&to=F`

Expected JSON result contains `212.0`.

## GitHub submission

Create a new **public** GitHub repository, for example:

**Repository name:** `temperature-converter`

**Description:**

> Python + Flask temperature converter for Celsius, Fahrenheit, and Kelvin with input validation, conversion formulas, automated tests, and Render deployment configuration.

Do not add a README, .gitignore, or license during GitHub repository creation because this project already contains its own README.

From PowerShell inside the project folder:

```powershell
git init
git branch -M main
git add .
git status
git commit -m "Build temperature converter"
git remote add origin https://github.com/YOUR_USERNAME/temperature-converter.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

After pushing, refresh the GitHub repository and confirm these important files are visible:

- `app.py`
- `templates/index.html`
- `static/style.css`
- `requirements.txt`
- `render.yaml`
- `.python-version`
- `tests/test_app.py`
- `README.md`

## Render deployment

The repository already contains `render.yaml`, so Render can use the project's deployment configuration.

### Dashboard method

1. Sign in to Render.
2. Connect your GitHub account.
3. Choose **New → Web Service**.
4. Select the `temperature-converter` GitHub repository.
5. Use the `main` branch.
6. If Render reads `render.yaml`, it will use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Health check: `/health`
   - Python version: `3.13.5`
7. Choose the Free plan if that is appropriate for your assignment.
8. Click **Create Web Service / Deploy**.
9. Wait for the deploy to finish successfully.
10. Open the generated `onrender.com` URL.
11. Test:
    - `0 °C → 32 °F`
    - `100 °C → 212 °F`
    - `0 °C → 273.15 K`
    - invalid value below absolute zero should show an error
12. Also open `/health` and confirm it returns `{"status":"ok"}`.

### Important

Render's production start command is `gunicorn app:app`. Do not use `python app.py` as the Render start command.

## Submission checklist

Before submitting to the internship portal, verify:

- [ ] GitHub repository is public.
- [ ] Project source code is pushed to GitHub.
- [ ] README explains the project, formulas, local setup, tests, and deployment.
- [ ] Render deployment is successful.
- [ ] Live Render URL opens correctly.
- [ ] Temperature conversions work.
- [ ] Invalid temperatures below absolute zero are rejected.
- [ ] `/health` works.
- [ ] GitHub repository link is copied correctly.
- [ ] Render live URL is copied correctly if the portal asks for it.
- [ ] Deployment configuration and rollback/deploy evidence are documented.
- [ ] LinkedIn post is published if required by the assignment.

## Rollback evidence

Render keeps deploy history. If a new deployment fails, the previously successful version remains the running version. For your submission, capture a screenshot of the Render **Deploys** page showing a successful deployment and keep it with your project evidence.

## Interview questions

### Why use functions for repeated calculations?

Functions keep each conversion operation separate, reusable, readable, and easier to test. They also avoid duplicating the same calculation logic in multiple places.

### What is a return statement?

A `return` statement sends a value from a function back to the code that called the function. The caller can store or use that returned value.

### What happens when a function does not explicitly return a value?

In Python, the function returns `None` automatically.

## Project structure

```text
temperature_converter_project/
├── app.py
├── requirements.txt
├── render.yaml
├── .python-version
├── README.md
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── tests/
    └── test_app.py
```

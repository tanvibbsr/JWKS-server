# JWKS-server
This Python project creates a RESTful JWKS server with FastAPI that offers public keys with unique identifiers (kid) for JWT verification. It also contains an authentication endpoint for issuing JWTs, which supports issuing JWTs with expired keys.

------------------------------------------------------------------------------------------------------------

Requirements:

- Python 3.10+
- Pip
- Git

------------------------------------------------------------------------------------------------------------

Setup / Run Locally:

1. Clone the repository
git clone https://github.com/<your-username>/jwks-server.git
cd jwks-server

2. Create and activate virtual environment
Windows + Git Bash
python -m venv venv
source venv/Scripts/activate

Mac / Linux
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the server

--------------------------------------------------------------------------------------------------------------

Tests:

Run tests with coverage:

pytest --cov=. --cov-report=term-missing


Expected Coverage:
 - Greater than 80%

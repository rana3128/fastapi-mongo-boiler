1. Create virtual environment 
    python -m venv test

2. Activate virtual environment 
    source test/bin/activate

3. Install dependency
    pip install -r requirements.txt

4. Create .env file and set value accordingly (reference .env.local)

4. Start service
    uvicorn main:app --reload --port 8001
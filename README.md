1. Create virtual environment:
    ```sh
    python -m venv test
    ```

2. Activate virtual environment:
    ```sh
    source test/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create .env file and set values accordingly (reference .env.local).

5. Start service:
    ```sh
    uvicorn main:app --reload --port 8001
    ```
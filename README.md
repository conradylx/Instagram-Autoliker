## Getting Started

Follow these steps to run the script:

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
2. **Activate the environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```
3. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```
4. \*\*Move example.env to .env
   ```bash
   mv ./example.env .env
   ```
5. **Run the script:**
   ```bash
   python main.py
   ```

> **Note:**
>
> - Store your login credentials in a `.env` file.
> - The script uses Chrome. Make sure you have the latest version of Chrome and the appropriate ChromeDriver installed.

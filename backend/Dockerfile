# 1. Use a lightweight Linux with Python 3.11
FROM python:3.11-slim

# 2. Set the folder inside the container
WORKDIR /app

# 3. Copy the dependencies list
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your "backend" folder into the container
# We copy specifically the 'app' folder to keep structure clean
COPY app /app/app

# 6. Open the port so we can talk to it
EXPOSE 8000

# 7. The Command to run the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


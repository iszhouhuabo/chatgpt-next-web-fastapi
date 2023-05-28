FROM python:3.9-slim-buster AS base
ENV OPENAI_API_KEY=""
ENV CODE=""
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "main.py" ]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

FROM python:3.10-alpine
COPY requirements.txt . 
RUN pip install -r requirements.txt
COPY mainscore.py utils.py score.txt .
CMD ["python", "mainscore.py"]

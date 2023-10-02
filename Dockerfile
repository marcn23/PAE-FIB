FROM python:alpine

RUN pip install pandas
RUN pip install pypdf[full]
RUN pip install pypdf2

WORKDIR /app

COPY in/ /app/in 
COPY fillpdf.py /app/fillpdf.py

VOLUME ["/app/in", "/app/out"]

CMD ["python3", "fillpdf.py"]
# RUN python3 fillpdf.py

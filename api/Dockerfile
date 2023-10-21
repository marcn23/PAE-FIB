FROM python:alpine

RUN pip install pandas
RUN pip install pypdf[full]
RUN pip install pypdf2
RUN pip install xlrd
RUN pip install xlwt
RUN pip install xlutils
RUN pip install flask
RUN pip install openpyxl
RUN pip install mysql-connector-python

WORKDIR /app

COPY main.py main.py
COPY in/ /app/in 
COPY fillpdf.py /app/fillpdf.py
COPY fillxlsx.py /app/fillxlsx.py
COPY fillpdf_program.py /app/fillpdf_program.py

VOLUME ["/app/in", "/app/out"]

EXPOSE 5000
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host", "0.0.0.0"]
# CMD ["python3", "fillpdf_program.py"]
# CMD ["python3", "fillpdf.py"]
#  CMD ["python3", "fillxlsx.py"]
FROM python:3.12-slim
WORKDIR /Zaluzhnyi
COPY . /Zaluzhnyi/
RUN pip install googletrans==3.1.0a0
CMD ["python", "gtrans3.py"]
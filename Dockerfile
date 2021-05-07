# syntax=docker/dockerfile:1
FROM python
WORKDIR /code
COPY . .
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
EXPOSE 3000
CMD ["python", "app.py"]
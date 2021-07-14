### Build docker image
#```
#build the image
#
#docker build -t mybi/sanic .
#
#and run
#
#docker run -p8000:8000 mybi/sanic
#
#```

# Compare sizes between this build:

#FROM python:3
#WORKDIR /app/
#COPY requirements.txt requirements.txt
#COPY src .
#RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["./app.py","--host=0.0.0.0"]

# and this one with multistage

# first stage
FROM python:3.8 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# second unnamed stage
FROM python:3.8-slim
WORKDIR /app/

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY src .

# update PATH environment variable
ENV PATH=/root/.local:$PATH

ENTRYPOINT ["python"]
CMD ["./app.py","--host=0.0.0.0"]



FROM python:3.7-buster

RUN groupadd -r grpc && useradd -r -g grpc grpc
WORKDIR /home/grpc

RUN python -m venv .venv

RUN .venv/bin/pip install -U pip
COPY requirements.txt requirements.txt
RUN .venv/bin/pip install -r requirements.txt

COPY . /home/grpc
RUN mkdir ./messages
RUN .venv/bin/python -m grpc_tools.protoc -I ./protobufs --python_out=./messages --grpc_python_out=./messages ./protobufs/*.proto

RUN chmod +x run.sh
RUN chown -R grpc:grpc ./
USER grpc

ENTRYPOINT ["./run.sh"]

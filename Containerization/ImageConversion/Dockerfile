ARG PYVERSION=3.11

FROM python:$PYVERSION

ENV PATH=/app/src/bin:$PATH

RUN apt update -y && apt install -y wget

ADD / /app/src



RUN pip3 install -r /app/src/requirements.txt

RUN mkdir -p /app/src/bin
RUN ln -sf /app/src/convert.py /app/src/bin/convert
RUN chmod +x /app/src/convert.py
RUN chmod +x /app/src/bin/convert

CMD ["/bin/bash"]


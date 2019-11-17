FROM python:3.8
ENV PYTHONPATH=/code:$PYTHONPATH
WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt


COPY restful_example /code/restful_example

ENTRYPOINT ["python3"]
CMD ["-m", "restful_example"]

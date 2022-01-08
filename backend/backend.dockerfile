FROM python:3.9-buster
WORKDIR /app/
ADD ./app/requirements.txt /app/requirements.txt
RUN pip3 install cython
RUN pip3 install -r /app/requirements.txt
ENV PYTHONPATH=/app
ADD ./app /app
RUN sed $'s/\r$//' ./prestart.sh > ./prestart.Unix.sh
RUN chmod +x prestart.Unix.sh
CMD ["/bin/sh", "prestart.Unix.sh"]
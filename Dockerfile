FROM python:3.6.0b2

RUN pip install --upgrade pip && \
    pip install ipython && \
    pip install requests==2.11.1 && \
    pip install requests-unixsocket && \
    pip install aiohttp

VOLUME /var/run/docker.sock:/var/run/docker.sock

CMD ipython

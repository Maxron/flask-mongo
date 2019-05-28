From kennethreitz/pipenv

ADD . /app

WORKDIR /app
RUN pipenv install

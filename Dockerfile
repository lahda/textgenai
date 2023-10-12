###########
# BUILDER #
###########

# pull official base image
FROM python:3.10 as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
RUN flake8 --exclude .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########
# pull official base image
FROM python:3.10

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup app && useradd app -g app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# install dependencies
# RUN apt update && apt add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic

# change to the app user
USER app

# run entrypoint.sh
# ENTRYPOINT ["/home/app/web/entrypoint.sh"]
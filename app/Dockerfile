# base image
FROM python:3.8.5
USER root

ARG project_dir=/var/www/

# workdir にファイル等追加
COPY requirements.txt $project_dir

# workdir
WORKDIR $project_dir

RUN apt-get update
RUN apt-get -y install locales && \
  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
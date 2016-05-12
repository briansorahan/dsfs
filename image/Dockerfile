FROM jupyter/scipy-notebook

USER root

RUN  apt-get update
RUN  apt-get -y install libxml2 libxslt1-dev sqlite3

USER $NB_USER

RUN  conda install --quiet --yes lxml=3.5.0 psycopg2=2.6.1
RUN  conda install -c IOOS --quiet --yes folium=0.2.0

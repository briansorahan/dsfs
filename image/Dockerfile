FROM jupyter/scipy-notebook

USER root

RUN  apt-get update
RUN  apt-get -y install libxml2 libxslt1-dev sqlite3 libgdal-dev

RUN  rm /bin/sh && ln -s /bin/bash /bin/sh

USER $NB_USER

RUN  . /opt/conda/envs/python2/bin/activate python2 && conda install \
         -c osgeo -c IOOS --quiet --yes folium=0.2.0 shapely=1.5.13 boto=2.40.0 gdal=1.11.4 geopandas=0.2.0.dev0

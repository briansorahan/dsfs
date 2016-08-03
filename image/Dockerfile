FROM jupyter/scipy-notebook

USER root

RUN  apt-get update
RUN  apt-get -y install libxml2 libxslt1-dev sqlite3 libgdal-dev libpq5

RUN  wget http://http.us.debian.org/debian/pool/main/libj/libjpeg8/libjpeg8_8d-1+deb7u1_amd64.deb && \
     dpkg -i libjpeg8_8d-1+deb7u1_amd64.deb

RUN  rm /bin/sh && ln -s /bin/bash /bin/sh

USER $NB_USER

# Install cloud libs
RUN  . /opt/conda/envs/python2/bin/activate python2 && \
     conda install -c anaconda --quiet --yes \
     boto=2.40.0

# Install geospatial libs
RUN  . /opt/conda/envs/python2/bin/activate python2 && \
     conda install -c asmeurer -c osgeo -c IOOS -c jjhelmus --quiet --yes \
     folium=0.2.0 shapely=1.5.13 pyproj=1.9.3 gdal=1.11.4 geopandas=0.2.0.dev0 geojsonio=0.0.2

# Install XML and HTML libs
RUN  . /opt/conda/envs/python2/bin/activate python2 && \
     conda install -c anaconda -c asmeurer --quiet --yes \
     lxml=3.6.0 beautiful-soup=4.3.2

# Install oauth libs
RUN  pip install oauthlib==1.1.2 requests-oauthlib==0.6.1

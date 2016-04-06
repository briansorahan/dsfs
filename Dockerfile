FROM		continuumio/anaconda
RUN		mkdir /projects
WORKDIR		/projects
COPY            . /projects
RUN             apt-get update
RUN             apt-get install sqlite3

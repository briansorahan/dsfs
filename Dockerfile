FROM		continuumio/anaconda
RUN		mkdir /projects
WORKDIR		/projects
COPY            . /projects

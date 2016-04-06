IMAGE           = bsorahan/tds
IPYTHON         = /opt/conda/bin/ipython
PYTHON2         = /opt/conda/bin/python2.7

# default target
all             : image

clean		:
		@rm -rf .image
		@docker rm -f weather_c

image		: .image
.image		: Dockerfile
		@docker build -t $(IMAGE) .
		@touch $@

py              : image
		@docker run -it $(IMAGE) $(PYTHON)

sh              : image
		@docker run -it $(IMAGE) /bin/bash

weather         :
.weather        : image
		@cat database.py | docker run -i --name weather_c $(IMAGE) $(PYTHON2)
		@docker cp weather_c:/projects/getting_started.db .

.PHONY		: all clean py sh

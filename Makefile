IMAGE           = bsorahan/tds
IPYTHON         = /opt/conda/bin/ipython
PYTHON2         = /opt/conda/bin/python2.7

# default target
all             : image

clean		:
		@rm -rf .image

image		: .image
.image		: Dockerfile
		@docker build -t $(IMAGE) . >/dev/null 2>/dev/null
		@touch $@

jupyter         :
		@docker run --rm -it -p 8888:8888 -v $(pwd):/notebooks jupyter/notebook

py              : image
		@docker run -it $(IMAGE) $(PYTHON)

sh              : image
		@docker run -it $(IMAGE) /bin/bash

weather         : .image database.py
		@docker rm -f weather_c >/dev/null 2>/dev/null || true
		@cat database.py | docker run -i --name weather_c $(IMAGE) $(PYTHON2)

.PHONY		: all clean jupyter py sh weather

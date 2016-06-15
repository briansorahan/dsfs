IMAGE           = bsorahan/ipynb
IPYTHON         = /opt/conda/bin/ipython
PYTHON2         = /opt/conda/bin/python2.7
PORT           ?= 8888

# default target
notebook        :
		@docker run --rm -it -p $(PORT):8888 -v $(shell pwd)/notebooks:/home/jovyan/work $(IMAGE)

all             : image

clean		:
		@rm -rf .image

image		: .image
.image		: Dockerfile
		@docker build -t $(IMAGE) . >/dev/null 2>/dev/null
		@touch $@

py              : image
		@docker run -it $(IMAGE) $(PYTHON)

sh              : image
		@docker run -it $(IMAGE) /bin/bash

.PHONY		: all clean jupyter py sh

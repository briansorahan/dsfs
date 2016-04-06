IMAGE           = bsorahan/tds

# default target
all             : image

clean		:
		@rm -rf .image

image		: .image
.image		: Dockerfile
		@docker build -t $(IMAGE) .
		@touch $@

py              : image
		@docker run -it $(IMAGE) /opt/conda/bin/ipython

sh              : image
		@docker run -it $(IMAGE) /bin/bash

.PHONY		: all clean py sh

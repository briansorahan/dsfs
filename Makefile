image		: .image
.image		: Dockerfile
		@docker build -t briansorahan/tds .
		@touch $@

.PHONY		: image

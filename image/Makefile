IMG=bsorahan/ipynb

clean:
	@rm -rf .image .push

image: .image

.image: Dockerfile
	@docker build -t $(IMG) .
	@touch $@

push: .push

.push: .image
	@docker push $(IMG)
	@touch $@

python:
	@docker run -it --rm $(IMG) python2

shell:
	@docker run -it --rm $(IMG) sh

.PHONY: clean image push shell

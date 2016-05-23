IMG=bsorahan/ipynb

image: .image

.image: Dockerfile
	@docker build -t $(IMG) .
	@touch $@

push: .push

.push: .image
	@docker push $(IMG)
	@touch $@

clean:
	@rm -rf .image .push

.PHONY: clean image push

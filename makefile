include .env

NS ?= mrjob
VERSION ?= latest

IMAGE_NAME ?= mrjob
CONTAINER_NAME ?= mrjob
CONTAINER_INSTANCE ?= default

.PHONY: default
default: help;

help:     ## Show this help.
	@echo '--------------------------------------------------------------------------------'
	@echo 'MRJob'
	@echo '--------------------------------------------------------------------------------'
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
	@echo '--------------------------------------------------------------------------------'

build:    ## Build the project image from the Dockerfile
	@unzip -o data/shortjokes_small.zip -d data/
	@unzip -o data/shortjokes_complete.zip -d data/
	@docker build -t $(NS)/$(IMAGE_NAME):$(VERSION) -f docker/mrjob/Dockerfile .

shell:    ## Run bash interactively in the container
	@docker run --rm --name $(CONTAINER_NAME)-$(CONTAINER_INSTANCE) -i -t $(PORTS) $(VOLUMES) $(ENV) $(NS)/$(IMAGE_NAME):$(VERSION) /bin/bash

notebook: ## Start a jupyter notebook stack
	@docker run -it --rm -p 8888:8888 jupyter/minimal-notebook

#!/bin/bash

PYNETEM_VERSION=0.15.0

docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 \
	-t mroy31/pynetem-frr-enac:$PYNETEM_VERSION \
	--push -f docker/alpine/Dockerfile .


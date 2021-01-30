#!/bin/bash

# to install cross compile
# if you docker container to register/install qemu-user (needed after reboot)
# docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
# if you want to use debian version of qemu-user
# aptitude install qemu-user-static binfmt-support

# docker buildx create --name cross-compile --use
# docker buildx ls
# docker buildx inspect --bootstrap

PYNETEM_VERSION=0.15.0

docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 \
	-t mroy31/pynetem-frr-enac:$PYNETEM_VERSION \
	--push -f docker/alpine/Dockerfile .


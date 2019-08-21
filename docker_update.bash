#!/bin/bash
image="registry.gitlab.com/kancom/letsmeet"

docker build  -f docker/Dockerfile -t "$image" .
docker push "$image"


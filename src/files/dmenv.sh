#!/bin/sh

if [ -z $1 ]; then
  echo "You have to specify docker machine"
  exit 1
fi

COMMAND="docker-machine env ${1}"
eval $COMMAND


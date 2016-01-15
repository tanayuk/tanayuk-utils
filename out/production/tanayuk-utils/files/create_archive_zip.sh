#!/bin/sh

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 (Archive file name) (To be archived file/directory)"
  exit 1
fi


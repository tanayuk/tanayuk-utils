#!/bin/sh

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 (Archive file name) (To be archived file/directory)"
  exit 1
fi
ARCHIVE_FILE=$1
TARGET=$2
PASSWORD=$(date|md5|head -c8)

echo "Generated password below"
echo ${PASSWORD}

if [[ -d ${TARGET} ]]; then
  zip -er ${ARCHIVE_FILE} ${TARGET} --password ${PASSWORD}
elif [[ -f ${TARGET} ]]; then
  zip -e ${ARCHIVE_FILE} ${TARGET} --password ${PASSWORD}
fi
echo "Completed archiving"

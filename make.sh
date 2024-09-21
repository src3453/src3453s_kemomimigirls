#!/bin/sh

VERSION_MAJOR=0
VERSION_SUFFIX="a"
VERSION_REVISION=$(git rev-list HEAD --count)
VERSION_HASH=$(git log -1 --format=%H | cut -c 1-7)
VERSION="v${VERSION_MAJOR}.${VERSION_REVISION}${VERSION_SUFFIX}.${VERSION_HASH}"
rm ./pack.mcmeta
cat ./pack.mcmeta.in | sed "s/VERSION/${VERSION}/" >> ./pack.mcmeta
zip "s3KmG${VERSION}.zip" -r ./assets/** ./pack.png ./pack.mcmeta
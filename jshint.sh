#!/bin/sh
set -e

if [ ! -f /usr/share/java-utils/java-functions ]; then
	echo >&2 "jpackage-utils not found."
	exit 1
fi
. /usr/share/java-utils/java-functions

set_javacmd
rhino=$(find-jar js)

exec $JAVACMD -jar $rhino /usr/share/jshint/env/rhino.js "$@"

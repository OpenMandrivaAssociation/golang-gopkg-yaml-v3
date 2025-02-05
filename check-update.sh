#!/bin/sh
curl "https://github.com/go-yaml/yaml/tags" 2>/dev/null |grep "tag/v3" |sed -e 's,.*tag/v,,;s,\".*,,;' |head -n1


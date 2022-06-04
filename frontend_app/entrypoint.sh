#!/bin/bash
cp -r /usr/src/cache/node_modules /app
chmod -R 777 node_modules/
exec yarn serve
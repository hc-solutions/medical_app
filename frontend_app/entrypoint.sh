#!/bin/bash
cp -r /usr/src/cache/node_modules /app
exec yarn serve

#!/bin/sh

rsync -zvhr --exclude 'venv' $(pwd)/* spider.local:~/python/raspberrypi/
#!/bin/sh

SCRIPT_PATH=$(dirname "$PWD/$0")
#ROOT=$(dirname "$SCRIPT_PATH")
ROOT=$SCRIPT_PATH

echo $ROOT

curl https://raw.github.com/pypa/virtualenv/master/virtualenv.py > virtualenv.py

python virtualenv.py "$ROOT/.env"
source "$ROOT/.env/bin/activate"

export ARCHFLAGS="-arch i386 -arch x86_64"
pip install versiontools
pip install nose #for tests
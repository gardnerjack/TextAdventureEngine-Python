#!/bin/bash

USAGE="Usage: create.sh <game information directory>"

if [ ! -z $1 ] ; then
    if [ -d $1 ] ; then
        rm -rf src/game_info
        cp -R $1 src/game_info
        echo "Run play.py to play the game"
    else
        echo "Not a directory"
        echo ${USAGE}
    fi
else
    echo ${USAGE}
fi
#!/usr/bin/bash

USER="millergl89@gmail.com"
NAME="millergl89"

git config --global --list

git config --global user.email ${USER}
git config --global user.name ${NAME}

git config --global --list

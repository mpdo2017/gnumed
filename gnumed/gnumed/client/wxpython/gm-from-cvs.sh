#!/bin/sh

# $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/client/wxpython/Attic/gm-from-cvs.sh,v $
# $Revision: 1.2 $

# start kvkd
# FIXME: needs logic to prevent more than one kvkd from running

# maybe force some locale setting here
#export LANG=fr

cd ../../
ln -vfsn client Gnumed
cd -
export PYTHONPATH="${PYTHONPATH}:../../"
python gnumed.py --debug --log-file=gm-from-cvs.log

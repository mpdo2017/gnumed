#!/bin/sh

# this tool can be used to generate a *.po file from all the gnumed client source
# $Source: /home/ncq/Projekte/cvs2git/vcs-mirror/gnumed/gnumed/client/locale/Attic/create_po_file.sh,v $
# $Revision: 1.2 $

# where to look for files
BASE="../"

find $BASE -name '*.py' -print0 | xargs -0 pygettext.py -v -o gnumed.po "-"

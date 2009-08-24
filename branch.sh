#!/bin/sh

set -x
prog=koffice
ver=1.6.3
branch=1.6

filter() {
	set -x
	# - filter out already patched files (regenerated tarball???)
	filterdiff -x krita/core/kis_perspective_math.cpp | \
	filterdiff -x kspread/plugins/scripting/kspreadcore/krs_cell.cpp | \
	filterdiff -x kspread/plugins/scripting/kspreadcore/krs_cell.h | \
	# - remove rcs id
	sed -e 's/$''Id:.*$/$''Id$/'
}

svn diff \
	svn://anonsvn.kde.org/home/kde/tags/$prog/$ver/$prog \
	svn://anonsvn.kde.org/home/kde/branches/$prog/$branch/$prog \
	| filter > $prog-branch.diff

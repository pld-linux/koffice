#!/bin/sh

set -x
pkg=koffice
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
	svn://anonsvn.kde.org/home/kde/tags/$pkg/$ver/$pkg \
	svn://anonsvn.kde.org/home/kde/branches/$pkg/$branch/$pkg \
	| filter > $pkg-branch.diff.tmp

d=$(interdiff $pkg-branch.diff{,.tmp} | wc -l)
if [ "$d" = 0 ]; then
	echo >&2 "$pkg-branch.diff: no new changes, skip"
	rm $pkg-branch.diff.tmp
	exit
fi

mv $pkg-branch.diff.tmp $pkg-branch.diff
echo >&2 "Updated $pkg-branch.diff"

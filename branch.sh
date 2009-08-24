#!/bin/sh

set -x
prog=koffice
ver=1.6.3
branch=1.6

svn diff \
	svn://anonsvn.kde.org/home/kde/tags/$prog/$ver/$prog \
	svn://anonsvn.kde.org/home/kde/branches/$prog/$branch/$prog \
	> koffice-branch.diff

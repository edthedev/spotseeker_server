#	$URL: https://svn-sdg.cites.illinois.edu:4430/Develop/Product/SDGPython/trunk/module/sdg/django/bluestem/templates/Makefile.am $
#	$Revision: 23174 $ $Date: 2011-04-28 15:16:43 -0500 (Thu, 28 Apr 2011) $

#	Copyright (c) 2008-2010 by Jon Roma and the Board of Trustees of the
#	University of Illinois.  All rights reserved.

CLEANFILES 		= $(COMPILED)

EXTRA_DIST 		= 

moduledir		= $(pythondir)/sdg/django/bluestem/templates

module_DATA		= 

SUBDIRS			= admin auth

%.pyc: %.py
	@echo "compiling $(subdir)/$<"
	@${PYTHON} -c "import py_compile; py_compile.compile('$<', '$@', doraise=True)"


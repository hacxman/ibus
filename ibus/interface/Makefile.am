# vim:set noet ts=4:
#
# ibus - The Input Bus
#
# Copyright (c) 2007-2010 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2007-2010 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

ibus_interface_PYTHON = \
	iconfig.py \
	ienginefactory.py \
	iengine.py \
	iibus.py \
	iinputcontext.py \
	ipanel.py \
	inotifications.py \
	__init__.py \
	$(NULL)

ibus_interfacedir = @pkgpythondir@/interface

CLEANFILES = \
	*.pyc \
	$(NULL)


-include $(top_srcdir)/git.mk

#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2018, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
""" Integrate Bokeh extensions into Sphinx autodoc.

Ensures that autodoc directives such as ``autoclass`` automatically
use Bokeh-specific directives (e.g., ``bokeh-prop`` and ``bokeh-model``)
when appropriate.

"""

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports
from six import class_types
from sphinx.ext.autodoc import AttributeDocumenter, ClassDocumenter, ModuleLevelDocumenter

# Bokeh imports
from bokeh.colors.color import Color
from bokeh.model import Model
from bokeh.core.enums import Enumeration
from bokeh.core.property.descriptors import PropertyDescriptor

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'ColorDocumenter',
    'EnumDocumenter',
    'ModelDocumenter',
    'PropDocumenter',
    'setup',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

class ColorDocumenter(ModuleLevelDocumenter):
    directivetype = 'bokeh-color'
    objtype = ''
    priority = 20

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, Color)

class EnumDocumenter(ModuleLevelDocumenter):
    directivetype = 'bokeh-enum'
    objtype = 'enum'
    priority = 20

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, Enumeration)

class PropDocumenter(AttributeDocumenter):
    directivetype = 'bokeh-prop'
    objtype = 'prop'
    priority = 20
    member_order = -100 # This puts properties first in the docs

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, PropertyDescriptor)

class ModelDocumenter(ClassDocumenter):
    directivetype = 'bokeh-model'
    objtype = 'model'
    priority = 20

    @classmethod
    def can_document_member(cls, member, membername, isattr, parent):
        return isinstance(member, class_types) and issubclass(member, Model)

def setup(app):
    app.add_autodocumenter(ColorDocumenter)
    app.add_autodocumenter(EnumDocumenter)
    app.add_autodocumenter(PropDocumenter)
    app.add_autodocumenter(ModelDocumenter)

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

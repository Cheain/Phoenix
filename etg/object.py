#---------------------------------------------------------------------------
# Name:        object.py
# Author:      Robin Dunn
#
# Created:     9-Nov-2010
# RCS-ID:      $Id:$
# Copyright:   (c) 2010 by Total Control Software
# Licence:     wxWindows license
#---------------------------------------------------------------------------

PACKAGE   = "wx"   
MODULE    = "_core"
NAME      = "object"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ 
    'wxRefCounter',
    'wxObject',       
    'wxClassInfo',
]    
    
#---------------------------------------------------------------------------
# Parse the XML file(s) building a collection of Extractor objects

import etgtools
module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
etgtools.parseDoxyXML(module, ITEMS)

#---------------------------------------------------------------------------
# Tweak the parsed meta objects in the module object as needed for customizing
# the generated code and docstrings.

import etgtools.tweaker_tools
etgtools.tweaker_tools.ignoreAssignmentOperators(module)
etgtools.tweaker_tools.removeWxPrefixes(module)


module.find('wxObject.operator delete').ignore()
module.find('wxObject.operator new').ignore()
module.find('wxCreateDynamicObject').ignore()


module.find('wxClassInfo').abstract = True
module.find('wxClassInfo.wxClassInfo').ignore()

module.find('wxRefCounter.~wxRefCounter').ignore(False)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# Run the generators

# Create the code generator and make the wrapper code
wg = etgtools.getWrapperGenerator()
wg.generate(module)

# Create a documentation generator and let it do its thing
dg = etgtools.getDocsGenerator()
dg.generate(module)

#---------------------------------------------------------------------------
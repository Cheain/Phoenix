#---------------------------------------------------------------------------
# Just some base classes and stubs for the various generators


class WrapperGeneratorBase(object):
    def __init__(self):
        pass    
    def generate(self, module, destFile=None):
        raise NotImplementedError
        
    
class DumpWrapperGenerator(WrapperGeneratorBase):
    """This one is just for debugging"""
        
    def generate(self, module, destFile=None):
        print "\n----------------------------------------------------------"
        print "Dump of Module Objects"
        print "----------------------------------------------------------"
        module.dump()
        
        

class DocsGeneratorBase(object):
    def __init__(self):
        pass        
    def generate(self, module):
        raise NotImplementedError
    
    
class StubbedDocsGenerator(DocsGeneratorBase):
    def generate(self, module):
        pass

#---------------------------------------------------------------------------        
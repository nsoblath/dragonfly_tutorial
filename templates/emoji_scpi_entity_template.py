from dripline.core import calibrate
from dripline.implementations import SimpleSCPIEntity

import logging
logger = logging.getLogger(__name__)

__all__ = []

__all__.append('Scientizer3000Entity')
class Scientizer3000Entity(SimpleSCPIEntity):
    '''
    '''

    def __init__(self,
                 **kwargs):
        '''
        Args: none
        '''
        SimpleSCPIEntity.__init__(self, **kwargs)

    @calibrate()
    def on_get(self):
        ...
        
    def on_set(self, value):
        ...

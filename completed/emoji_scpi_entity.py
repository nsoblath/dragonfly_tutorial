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
        to_send = [Scientizer3000Entity.convert_to_emoji(self.cmd_base + '?')]
        result = self.service.send_to_device(to_send)
        result = Scientizer3000Entity.convert_from_emoji(result)
        logger.debug(f'raw result is: {result}')
        return result

    def on_set(self, value):
        to_send = [Scientizer3000Entity.convert_to_emoji(f'{self.cmd_base} {value};{self.cmd_base}?')]
        return Scientizer3000Entity.convert_from_emoji(self.service.send_to_device(to_send))

    dict_from_emoji = {
        "💮": "0", 
        "🏞": "1",
        "🍚": "2",
        "🗿": "3", 
        "🎆": "4", 
        "🐳": "5", 
        "🔈": "6", 
        "📒": "7", 
        "🔨": "8", 
        "🌏": "9", 
        "☕": "a", 
        "📈": "b", 
        "😨": "c", 
        "👘": "d", 
        "💹": "e", 
        "👗": "f", 
        "💋": "g", 
        "🌤": "h", 
        "🚼": "i", 
        "🎡": "j", 
        "☦": "k", 
        "🕣": "l", 
        "🚷": "m", 
        "🐥": "n", 
        "🌹": "o", 
        "➕": "p", 
        "🅿": "q", 
        "☄": "r", 
        "🚟": "s", 
        "👽": "t", 
        "🍫": "u", 
        "🚜": "v", 
        "🏄": "w", 
        "✏": "x", 
        "🍀": "y", 
        "🎴": "z",
        "❓": "?",
        "🎍": " ",
        "🐿": ".",
        "🍇": ",",
        "🔖": ":",
        "🐹": ";",
        "🌌": "_",
        "😝": "-",
        "↩": "\n",
    }

    dict_to_emoji = {v:k for k,v in dict_from_emoji.items()}

    def convert_from_emoji(my_string):
        converted_list = [Scientizer3000Entity.dict_from_emoji[item] for item in list(my_string)]
        return ''.join(converted_list)

    def convert_to_emoji(my_string):
        converted_list = [Scientizer3000Entity.dict_to_emoji[item] for item in list(my_string.casefold())]
        return ''.join(converted_list)
    
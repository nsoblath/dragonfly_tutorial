# Scientizer 3000

Congratulations on your purchase of the Scientizer 3000!!!  It's s much better, it deserves more exclamation points!!!!!!

## Interface

This device implements an interface that's compatible with the basic aspecs of the SCPI standard.  In particular, it does not pay attention to the tree hierarchy of commands, or handle multiple simultaneous commands.

Also, all SCPI messages to the device, and those sent from the device, are enocded as a fixed set of emojis.  Because who doesn't want a little more color and variety in their network communications?  The conversion table in use is below.

### Available commands

* IDN: get -- returns information about the device
* OPT: get -- returns the available options (not actually relevant to options you can use)
* READ: get and set -- set or return the "reading"
* VOLTage: get and set -- set or return the voltage
* FREQuency: get and set -- set or return the frequency

### Emoji conversion table

```
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
```

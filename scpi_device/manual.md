# Scientizer 1.0

Congratulations on your purchase of the Scientizer 1.0!  You're well on your way to the best science!

## Interface

This device implements an interface that's compatible with the basic aspecs of the SCPI standard.  In particular, it does not pay attention to the tree hierarchy of commands, or handle multiple simultaneous commands.

### Available commands

* IDN: get -- returns information about the device
* OPT: get -- returns the available options (not actually relevant to options you can use)
* READ: get and set -- set or return the "reading"
* VOLTage: get and set -- set or return the voltage
* FREQuency: get and set -- set or return the frequency

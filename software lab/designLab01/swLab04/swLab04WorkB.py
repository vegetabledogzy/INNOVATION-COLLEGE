import lib601.poly as poly
import swLab04SignalDefinitions
reload(swLab04SignalDefinitions) # so changes you make in swLab04SignalDefinitions.py will be reloaded
from swLab04SignalDefinitions import *

usamp=UnitSampleSignal()
polyR(usamp, poly.Polynomial([3, 5, -1, 0, 0, 3, -2])).plot(-5,50)

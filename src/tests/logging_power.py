# This script is used on the devices themselves to log power usage
from jtop import jtop

with jtop() as jetson:
    # jetson.ok() will provide the proper update frequency
    while jetson.ok():
        # Read tegra stats
        print(jetson.stats['time'], ": ", jetson.stats['Power TOT'])


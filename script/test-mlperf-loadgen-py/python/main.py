﻿"""
Testing MLPerf loadgen

# Developer(s): Grigori Fursin
"""

# Import cmind to test break points
import cmind.utils

import numpy as np

cmind.utils.debug_here(__file__, port=5678, text='Debugging loadgen!', env_debug_uid='a83d9c76755a40af')

print ('- Importing MLPerf loadgen library ...')
import mlperf_loadgen as lg
print ('  SUCCESS!')


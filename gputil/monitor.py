import gputil.GPUtil as GPUtil
import time
from datetime import datetime

def Monitor(delay, guard=None):
    while(1):
        status = GPUtil.getAvailability(GPUtil.getGPUs())
        if any(status):
            if guard is None:
                return status.index(1)
            elif status[guard] is not 0:
                return guard
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "| NO GPU")
        time.sleep(delay)




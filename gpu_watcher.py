from gputil.monitor import  Monitor
import os

if __name__=='__main__':
    monitor = Monitor(1)
    os.environ["CUDA_VISIBLE_DEVICES"] = str(monitor)
    # run your script
    os.system("CUDA_HOME_VISIBLE_DEVICES=" + str(monitor) + " krenew python3 GANframework.py")


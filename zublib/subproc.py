from datetime import datetime
from multiprocessing import Process
import os, sys, logging

def setup_working_directory ( directory ):
    """check if the given directory exists, if not attempt to create it."""
    if not os.path.isdir(directory):
        print 'creating directory @ %s' % directory,
        os.mkdir(directory)
        if os.path.isdir(directory): print 'SUCCESS!'
        else:
            print 'FAILED!'
            sys.exit(0)
    os.chdir(directory)

def setup_logging ( ):
    """turn on logging in the current working directory"""
    log_file_extension = ".log"
    t = datetime.now()
    tstr = "%s.%s.%s_%s:%s:%s" % (t.month, t.day, t.year, t.hour, t.minute, t.second)
    file_name = tstr + log_file_extension
    file_path = os.path.join(os.getcwd(), file_name)
    print "logging to %s" % file_path
    logging.basicConfig(filename=file_name, level=logging.INFO)

def dispatch_child_proc ( function, directory=None, logging=False , block=False ):
    """setup a child process to execute the given function. optional arguments
    are a working directory and if to set up logging to a file"""
    if logging:
        setup_logging()
    if directory:
        setup_working_directory(directory)
    p = Process(target=function)
    p.start()
    if block:
        p.join()

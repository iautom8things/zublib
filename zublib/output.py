import sys, os
from time import time
from datetime import datetime

def get_seperated_string (seperator, *args ):
    """return a string of each argument seperated by a tab char"""
    return seperator.join(map(str, args))

def record_data ( list, seperator, *args ):
    """append information to DATA list"""
    list.append( get_seperated_string(seperator,*args) )

def write_output ( data, out_folder, name, link=False ):
    add_newline = lambda x: str(x) + "\n"
    # add newline characters to the end of each of the data items
    data = map(add_newline, data)
    # get a string representation of the date
    outfile = name + "_" + str(datetime.fromtimestamp(time()))
    out_path = os.path.join(out_folder, outfile)
    # write the data to the log
    with open(out_path, 'w') as f:
        f.writelines(data)
    if link:
        # update symlink latest to point to latest
        latest_path = os.path.join(out_folder, 'latest')
        command = 'ln -fs "%s" "%s"' % (out_path, latest_path)
        # execute the symlink command
        os.system(command)

def print_status ( pos, max_val, width=2, percentage=5 ):
    """Given two integers display a status bar that looks like:

        -[==================                      ]- 48% [586/1200]
        Where pos = 586 and max_val = 1200

        Requires:
            pos >= 0
            max_van > pos

        If percentage isn't a divisor of 100 then status bar will finish
        before the process is actually completeif percentage isn't a divisor
        of 100 then status bar will finish before the process is actually
        complete.
        """
    total_divisions = 100/percentage
    ratio = int((pos*100.0)/max_val)
    num_div_completed = ratio / percentage
    bar = "=" * width * num_div_completed
    empty = " " * width * (total_divisions-num_div_completed)
    print "\r-[%s%s]- %d%% [%s/%s]" % (bar, empty, ratio, pos, max_val),
    if pos == max_val: print "\n"
    sys.stdout.flush() # This is needed since the printing is often done in a subprocess, otherwise you wouldn't see real-time progress

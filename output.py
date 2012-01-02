import sys

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

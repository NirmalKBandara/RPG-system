# This is for fun... :)

import time
import sys
import itertools


def loading_animation(duration=5):
    spinner = itertools.cycle(['\\', '-', '/', '|'])
    
    end_time = time.time() + duration
    
    while time.time() < end_time:
        char = next(spinner)
        
        sys.stdout.write(f'\rLoading... {char}')
        
        sys.stdout.flush()
        
        time.sleep(0.1)
    
    sys.stdout.write('\rDone!          \n')

if __name__ == "__main__":
    loading_animation()

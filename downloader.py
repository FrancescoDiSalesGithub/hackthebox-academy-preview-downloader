import sys

from pywebcopy import save_webpage
import os


if __name__ == "__main__":
    path_current = os.getcwd()

    print(sys.argv[1])
    print(sys.argv[2])


    newfolder = path_current + "/" +sys.argv[1] + "/"

    kwargs = {'bypass_robots': True, 'project_name': sys.argv[1]+" dump",'open_in_browser':False}
    save_webpage(sys.argv[2], newfolder, **kwargs)




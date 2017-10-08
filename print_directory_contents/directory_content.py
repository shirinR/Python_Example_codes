def print_directory_contents(sDir):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    import os
    # from os import listdir
    # from os.path import isfile, join
    # from os.path import isdir, join

    for sChild in os.listdir(sDir):
        sChildDir = os.path.join(sDir,sChild)
        if os.isdir(sChildDir):
            print_directory_contents(sChildDir)
        else:
            print(sChildDir)

import os


class FindSource:
    

    def findsource(self, top, extension):
        '''Takes a root folder (top) and an extension type and searches all directories within that folder for files ending in that extension. Returns a list of fully qualified file names (starting with the root folder, of course)'''
        foundfiles = []
        for root, dirs, files in os.walk(top):
            for file in files:
                if file[-len(extension):] == extension:
                    foundfiles.append(str(root + os.sep + file))
        return foundfiles

if __name__ == '__main__':
    pass

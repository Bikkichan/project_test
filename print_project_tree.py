import os

# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def list_files(startpath):
     for root, dirs, files in os.walk(startpath):
         if '.git' in dirs:
             level = root.replace(startpath, '').count(os.sep)
             indent = ' ' * 4 * (level)
             print('{}{}/'.format(indent, os.path.basename(root)))
             subindent = ' ' * 4 * (level + 1)
             for f in files:
                 print('{}{}'.format(subindent, f))

startpath = os.getcwd()
list_files(startpath)
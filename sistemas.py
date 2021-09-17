import sys,os

print('ID do programa e o diretório de trabalho')
print(os.getpid(), os.getcwd())

print('sys')
print(sys.platform)

print('os')
print(os.environ.keys())
print(os.environ['GTK_BASEPATH'])
print(os.environ['APPDATA'])
print(os.environ['PYTHONPATH'])

x = os.pathsep, os.sep, os.pardir, os.curdir, os.linesep
print(x)
########################################################
caminho = os.getcwd() + os.sep + '107.py'
#
# print('os.path.isdir("ex") = ', os.path.isdir('ex'))
# print('os.path.isfile("ex") = ', os.path.isfile('ex'))
# print('os.path.exists("ex") = ', os.path.exists('ex'))
# print('os.path.exists("107.py") = ', os.path.exists('107.py'))
# print('os.path.getsize("107.py") = ', os.path.getsize('107.py'))
# print('os.path.split("%s") = ' % caminho, os.path.split(caminho))
# print('os.path.join("media", "107.py") = ', os.path.join("media", "107.py"))
# print('os.path.join("media", "107.py", "HD") = ', os.path.join("media", "107.py", 'HD'))
# print('os.path.dirname("%s") = ' % caminho, os.path.dirname(caminho))
# print('os.path.basename("%s") = ' % caminho, os.path.basename(caminho))
# print('os.path.splitext("107.py") = ', os.path.splitext("107.py"))
# print('os.path.normpath("media\\pedro\\HD\\Aulas/iz/aulas_python/107/107.py") = ',os.path.normpath("media\\pedro\\HD\\Aulas/iz/aulas_python/107/107.py"))
# print('os.path.abspath("") = ', os.path.abspath(""))
# print('os.path.abspath("ex") = ', os.path.abspath("ex"))
# print('os.path.abspath("%s")' % os.curdir, os.path.abspath("."))
# print('os.path.abspath("%s")' % os.pardir, os.path.abspath(".."))
#####################################################################################################

print("s",os.popen('type cliente.py').read())


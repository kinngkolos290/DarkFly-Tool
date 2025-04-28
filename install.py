#!/usr/bin/python3

"""
Author             : Ms.ambari
contact            : ambari.developer@gmail.com
Github             : https://github.com/Ranginang67
my youtube channel : Ms.ambari

subcribe my youtube Channel to learn ethical Hacking ^_^
"""

import sys
import os.path
import subprocess

ntfile = ['.module', 'lib']

with open('.module/jalurU.ms', 'r') as file:
    ubuntu = file.read().strip()
with open('.module/jalurT.ms', 'r') as file:
    termux = file.read().strip()
with open('.module/ngentot.ms', 'r') as file:
    termlb = file.read().strip()
with open('.module/IN.ms', 'r') as file:
    instal = file.read().strip()


def _main_():
    if os.path.isdir(ubuntu):
        if os.getuid() != 0:
            print('[x] Failed: your must be root')
            sys.exit()

        if not os.path.isdir(ntfile[0]):
            print('[x] Failed: no directory module')
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print('[x] Failed: no directory lib')
            sys.exit()
        else:
            print(instal)

            # ==================================================================#
            os.system('python3 .module/files/' + str(open('.module/A.ms').read()))
            os.system('python3 .module/files/' + str(open('.module/B.ms').read()))
            os.system('python3 .module/files/' + str(open('.module/C.ms').read()))
            os.system('python3 .module/files/' + str(open('.module/D.ms').read()))
            os.system('python3 .module/files/' + str(open('.module/E.ms').read()))
            os.system('python3 .module/files/' + str(open('.module/F.ms').read()))
            os.system('python3 .module/files/' + str(open('.module/G.ms').read()))
            os.system('python3 .module/files/' + str(open('.module/H.ms').read()))

            # ==================================================================#

            if os.path.isdir('/usr/bin/lib'):
                os.system('rm -rf /usr/bin/lib')
                os.system(open('.module/pindahU.ms').read())
                os.system(open('.module/PindahU.ms').read())

            if not os.path.isdir('/usr/bin/lib'):
                os.system(open('.module/pindahU.ms').read())
                os.system(open('.module/PindahU.ms').read())

            # ==================================================================#

            print(open('.module/DU.la').read())
            print(open('.module/Du').read())
            os.system('python3 .JM.xn')

            # ==================================================================#

    if os.path.isdir(termux):
        if not os.path.isdir(termux):
            sys.exit()

        if not os.path.isdir(ntfile[0]):
            print('[x] Failed: no directory module')
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print('[x] Failed: no directory lib')
            sys.exit()
        else:
            print(instal)

            # ==============================================================#
            os.system('python2 .module/' + str(open('.module/A.ms').read()))
            os.system('python2 .module/' + str(open('.module/B.ms').read()))
            os.system('python2 .module/' + str(open('.module/C.ms').read()))
            os.system('python2 .module/' + str(open('.module/D.ms').read()))
            os.system('python2 .module/' + str(open('.module/E.ms').read()))
            os.system('python2 .module/' + str(open('.module/F.ms').read()))
            os.system('python2 .module/' + str(open('.module/G.ms').read()))
            os.system('python2 .module/' + str(open('.module/H.ms').read()))

            # ==============================================================#

            if os.path.isdir(termlb):
                os.system(open('.module/pacar.ms').read())
                os.system(open('.module/pindahT.ms').read())
                os.system(open('.module/PINDAHT.txt').read())

            if not os.path.isdir(termlb):
                os.system(open('.module/pindahT.ms').read())
                os.system(open('.module/PINDAHT.txt').read())

            # ==============================================================#

            print(open('.module/DU.la').read())
            print(open('.module/Du').read())
            os.system('python2 .JM.xn && cd')

            # ==============================================================#

if __name__ == '__main__':
    _main_()

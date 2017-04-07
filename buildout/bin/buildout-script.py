#!"e:\python\python.exe"

import sys
sys.path[0:0] = [
  'e:\\python\\lib\\site-packages',
  ]

import zc.buildout.buildout

if __name__ == '__main__':
    sys.exit(zc.buildout.buildout.main())

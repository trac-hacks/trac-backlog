__version__ = (0, 5, 1, 'dev', 1)

def get_version():
   version = '%d.%d.%d' % __version__[0:3]
   if __version__[3]:
       version = '%s-%s%s' % (version, __version__[3],
                              (__version__[4] and str(__version__[4])) or '')
   return version


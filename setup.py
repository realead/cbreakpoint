from distutils.core import setup
from distutils.extension import Extension


import platform


if platform.system() == 'Windows':
    extra_compile_args = ["/Od"]
else:
    extra_compile_args = ["-O0"]




try:
   from Cython.Build import cythonize
   extensions = [
    Extension("cbreakpoint", ["src/cbreakpoint.pyx"],
        extra_compile_args=extra_compile_args),
   ]
   extensions =  cythonize(extensions, language_level = "3")
except ImportError:
   #fall back to pre-generated c-file:
   extensions = [
    Extension("cbreakpoint", ["src/cbreakpoint.c"],
        extra_compile_args=extra_compile_args),
   ]



kwargs = {
      'name':'cbreakpoint',
      'version':'0.1.0',
      'description':'a tool for setting c-breakpoints in py-scripts',
      'author':'Egor Dranischnikow',
      'url':'https://github.com/realead/cbreakpoint',
      'license': 'MIT',
      'ext_modules':  extensions
}

setup(**kwargs)


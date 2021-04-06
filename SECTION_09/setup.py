from distutils.core import setup, Extension

setup(name="star", 
      ext_modules=[
        Extension("star",
                  ["star.c"],
                  include_dirs = ['.'],
                  )
        ]
)

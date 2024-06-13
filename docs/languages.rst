Architecture Support
====================

.. ipython::

   In [0]: for arch in pypcode.Arch.enumerate():
      ...:     for lang in arch.languages:
      ...:         print(f'{lang.id:32} - {lang.description}')

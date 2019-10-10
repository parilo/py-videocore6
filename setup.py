
from distutils.core import setup
from Cython.Build import cythonize


setup(
        name = 'py-videocore6',
        packages = ['videocore6'],
        version = '0.0.0',
        description = 'Python library for GPGPU programming on Raspberry Pi',
        author = 'Sugizaki Yukimasa',
        author_email = 'ysugi@idein.jp',
        ext_modules = cythonize(
                module_list = 'videocore6/buffer_to_ptr.pyx',
                compiler_directives = {
                        'language_level' : 3,
                },
        ),
)
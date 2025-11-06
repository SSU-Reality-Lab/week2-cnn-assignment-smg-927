from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        name='utils.im2col_cython',                  # 패키지 경로 반영
        sources=['utils/im2col_cython.pyx'],         # 파일 위치 반영
        include_dirs=[np.get_include()],
        language="c",
    ),
]

setup(
    name="cs231n_utils_local",
    ext_modules=cythonize(
        extensions,
        language_level="3"
    ),
)

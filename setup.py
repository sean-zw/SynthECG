# setup.py
from setuptools import setup, find_packages
import torch.cuda
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
from torch.utils.cpp_extension import CUDA_HOME

# Set up CUDA extension if CUDA is available
ext_modules = []
if torch.cuda.is_available() and CUDA_HOME is not None:
    extension = CUDAExtension(
        'cauchy_mult', [
            'extension/cauchy/cauchy.cpp',
            'extension/cauchy/cauchy_cuda.cu',
        ],
        extra_compile_args={'cxx': ['-g', '-march=native', '-funroll-loops'],
                            'nvcc': ['-O2', '-lineinfo', '--use_fast_math']}
    )
    ext_modules.append(extension)

setup(
    name="SYNTHECG",
    version="1.0",
    packages=find_packages(),
    ext_modules=ext_modules,
    cmdclass={'build_ext': BuildExtension} if ext_modules else {},
    zip_safe=False  # Required for C extensions
)
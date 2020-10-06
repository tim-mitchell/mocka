from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='mocka',
    version='1.0.0',  # Required
    description='A unittest mock library than understands annotations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tim-mitchell/mocka',
    author='Tim Mitchell',
    author_email='tim.mitchell@seequent.com',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing :: Mocking',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='test unittest mock protocol annotation',
    py_modules=["mocka"],
    python_requires='>=3.6, <4',
    install_requires=[],
    project_urls={
        'Source': 'https://github.com/tim-mitchell/mocka/',
    },
)

from setuptools import setup, find_packages

setup(
    name='x_com_ufo_defense',
    version='19.9.9',
    packages=find_packages(exclude=[ 'docs' ]),
    install_requires=[  'numpy',
                        'scipy',
                        'redis',
                        'flask',
                        'flask_cors'  ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Linux',
        'Topic :: UFO Defense',
    ),
    author='Sasha Elaine Fox'
)

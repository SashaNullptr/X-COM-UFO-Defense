from setuptools import setup, find_packages

setup(
    name='x_com',
    version='19.9.9',
    packages=find_packages(exclude=[ 'docs' ]),
    install_requires=['psycopg2','flask','flask_cors'],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Operating System :: Linux',
        'Topic :: UFO Defense',
    ),
    package_data={
      'x_com': ['config_files/*'],
      },
    author='Sasha Elaine Fox'
)

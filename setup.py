from setuptools import setup

setup(
    name='mealtagger',
    version='0.0.1',

    description='A simple tag creator for slovak meals.',

    url='https://github.com/hladny-matfyzak/meal-tagger',

    author='mr.Shu',
    author_email='mr@shu.io',

    maintainer='mr.Shu',
    maintainer_email='mr@shu.io',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Natural Language :: Slovak',

        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='lemmatization lemming slovak',

    packages=['mealtagger'],
    install_requires=['lemmsk'],
)

# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name='google_play_scraper',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='Google-Play-Scraper provides APIs to easily crawl the Google Play Store for Python without any external dependencies!.',

    # The project's main homepage.
    url='https://github.com/vy-labs/google-play-scraper',

    # Author details
    author='JoMingyu',
    author_email='jo.mingyu@gmail.com',

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='GooglePlayStore apk',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['google_play_scraper'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["aenum==3.1.11"],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [
            "isort==4.3.21"
            "autoflake==1.4"
        ]
    },
)

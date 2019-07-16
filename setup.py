from setuptools import setup

setup(
    name='google-play-scraper',
    version='0.1a',
    url='https://github.com/JoMingyu/google-play-scraper',
    license='MIT',
    author='PlanB',
    author_email='mingyu.planb@gmail.com',
    description='Google-Play-Scraper provides APIs to easily crawl the Google Play Store for Python without no external dependencies!',
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    packages=['google_play_scraper'],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown"
)

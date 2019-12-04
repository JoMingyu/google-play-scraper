from setuptools import setup, find_packages

from google_play_scraper import __version__

setup(
    name="google-play-scraper",
    version=__version__,
    url="https://github.com/JoMingyu/google-play-scraper",
    license="MIT",
    author="PlanB",
    author_email="mingyu.planb@gmail.com",
    description="Google-Play-Scraper provides APIs to easily crawl the Google Play Store"
    " for Python without any external dependencies!",
    classifiers=[
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Development Status :: 4 - Beta",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Typing :: Typed",
    ],
    packages=find_packages(exclude=["tests"]),
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
)

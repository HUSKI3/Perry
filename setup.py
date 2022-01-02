from distutils.core import setup, find_packages

setup(
    name="Perry",
    version="0.1.12",
    author="HUSKI3",
    author_email="ignispy@protonmail.com",
    description=""" A framework that let's you compose websites in Python with ease!   """,
    long_description_content_type="text/markdown",
    long_description=f"""{open('README.rst','r').read()}""",
    packages=find_packages('Perry'),
    url="http://pypi.python.org/pypi/Perry/",
    project_urls={
        "Bug Tracker": "https://github.com/HUSKI3/Perry/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       "Flask"
     ],
    python_requires=">=3.6",
)
import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


test_requirements = [
    "pytest>=3",
]

setuptools.setup(
    name="doeapi",
    version="0.0.1",
    author="Aldrin Navarro",
    author_email="aldrinnavarro16@gmail.com",
    description="DOE API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    keywords="doeapi",
    url="https://github.com/aldnav/doeapi",
    project_urls={
        "Bug Tracker": "https://github.com/aldnav/doeapi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "doeapi"},
    packages=setuptools.find_packages(where="doeapi"),
    python_requires=">=3.9",
    test_suite="tests",
    tests_require=test_requirements,
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="future-scientist",
    version="0.0.2",
    author="Senthil",
    author_email="senthil@example.com",
    description="teaching purpose",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/senthilskm983/future-scientist",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNUv3 ",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
        'Flask',
		'PyQt5'
      ],
    python_requires='>=3.6',
)

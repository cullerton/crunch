import setuptools

setuptools.setup(
    name="prog_test",
    version="0.0.1",
    author="mike cullerton",
    author_email="michaelc@cullerton.com",
    description="A small package for Crunch programming test",
    url="https://github.com/cullerton/crunch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

setup(
    name="Fleepy",
    version='0.1',
    description="Pythonic Fleep API Client",
    author="Nicholas Amorim",
    author_email="nicholas@alienretro.com",
    url="https://github.com/nicholasamorim/fleepy",
    license="GPL",
    packages=find_packages(),
    install_requires=['requests', 'attrdict'],
    tests_require=['mock', 'tox'],
    keywords='api consumer client fleep chat http rest',
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)


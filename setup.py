from setuptools import find_packages
from distutils.core import setup
from django3_keycloak.settings import VERSION
setup(
    name='django3_keycloak',
    version=VERSION,
    license='MIT',
    description='Django 3 Keycloak Integration',
    author='Ben Shearlaw',  # Type in your name
    include_package_data=True,
    install_requires=[
        "pyjwkest",
    ],
    packages=find_packages(),
    author_email='ben.shearlaw@atamate.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6, 3.8',
    ],
)

from setuptools import setup

setup(
    name='python-url-images',
    version='0.0.1',
    url='https://github.com/AndrewIngram/python-url-images',
    install_requires=[],
    description="URL-based manipulation of images",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Andrew Ingram",
    author_email="andy@andrewingram.net",
    packages=['url_images'],
    package_dir={'': '.'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python']
)
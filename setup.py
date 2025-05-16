from setuptools import setup, find_packages

setup(
    name='scl_sandhi_interface',
    version='0.1.0',
    description='Sanskrit Sandhi operations using Samsaadhanii's Sandhi engine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sriram Krishnan',
    author_email='sriramk8@gmail.com',
    packages=find_packages(),  # Automatically finds __init__.py files
    install_requires=[],
    python_requires='>=3.7',
)


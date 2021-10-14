import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='pysniffer',
    version='0.0.1',
    packages=setuptools.find_packages(),
    author='TCC',
    author_email='',
    description='Ferramenta desenvolvida para TCC',
    install_requires=required
)

import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()


setuptools.setup(
    name='pysniffer',
    version='0.0.1',
    packages=setuptools.find_packages(),
    author='Luana, Mariana, Sarah e Sinara',
    author_email='',
    description='Tool to analyze Python Projects',
    install_requires=required
)

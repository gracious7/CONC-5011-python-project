from setuptools import setup, find_packages

setup(
    name='CONC-5011-python-project-repository-setup',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here, e.g.
        # 'requests>=2.0',
    ],
)


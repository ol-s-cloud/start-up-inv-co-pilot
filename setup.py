from setuptools import setup, find_packages

setup(
    name='start-up-inv-co-pilot',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=open('requirements.txt').read().splitlines(),
    author='Olanrewaju Said',
    description='Start-up Funding Predictions with Ensemble Methods',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ol-s-cloud/start-up-inv-co-pilot',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
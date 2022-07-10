from setuptools import setup


setup(
    name='text_utils',
    version='0.0.1',
    install_requires=[
        'numpy>=1.23',
        'pandas>=1.4',
        'pyxDamerauLevenshtein>=1.7.0',
        'scikit-learn>=1.1'
    ]
)
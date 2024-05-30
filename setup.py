from setuptools import setup, find_packages

setup(
    name='dm_ai_model',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'sklearn',
        'joblib',
    ],
    author='BobryTeam',
    author_email='sinntexxx@gmail.com',
    description='Metrics data structure',
    url='https://github.com/BobryTeam/dm-ai-model',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
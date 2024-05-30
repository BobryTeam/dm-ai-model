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
        'trend_data @ git+https://github.com/BobryTeam/trend-data.git@pip-deps',
    ],
    author='BobryTeam',
    author_email='sinntexxx@gmail.com',
    description='Decision Module AI model',
    url='https://github.com/BobryTeam/dm-ai-model',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
from setuptools import setup, find_packages

setup(
<<<<<<< HEAD:exile-safework/setup.py
    name='exile-safework',
    version='1.0.4',
    author='PardhuSreeRushiVarma',
    description='Exile-SafeWork: A simulated red-team framework for educational and research use only.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(include=['core', 'modules', 'modules.*']),
    include_package_data=True,
    install_requires=[
        'rich',
        'pycryptodome',
    ],
    entry_points={
        'console_scripts': [
            'exile=exile:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Education',
        'Topic :: Security',
    ],
    python_requires='>=3.7',
=======
    name="exile-safework",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rich",
        "pycryptodome"
    ],
    entry_points={
        'console_scripts': [
            'exile = exile:main'
        ],
    },
>>>>>>> f0d56ee (Full Build):setup.py
)

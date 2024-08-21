from setuptools import setup, find_packages

setup(
    name='QANexusPY',
    version='0.1.0',
    description='A Python library for QA tasks, including assertions and data generation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Elie-A/QANexusPY',
    author='Elie Abdallah',
    author_email='elieabdallah961.com',
    license='MIT',
    packages=find_packages(), 
    install_requires=[
        # Add dependencies here, e.g., 'numpy>=1.19.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    zip_safe=False,
)
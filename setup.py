from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='CRO Tax Deptors',
    version='0.1.0',

    description='List of Croatian tax debtors',
    long_description=readme(),
    long_description_content_type='text/markdown',

    url='https://github.com/arrrlo/CRO-Tax-Deptors',
    licence='MIT',

    author='Ivan Arar',
    author_email='ivan.arar@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='croatia, tax, debt',

    packages=['cro_tax_deptors'],
    install_requires=[
        'click~=6.7',
        'colorama~=0.3',
        'db-transfer~=0.3.3',
        'requests~=2.18.4',
        'lxml==4.2.1',
        'python-slugify~=1.2.5',
        'pyfiglet~=0.7.5',
        'termcolor~=1.1.0',
    ],
    entry_points={
        'console_scripts': [
            'crotaxdeptors=cro_tax_deptors.cli:cli'
        ],
    },

    project_urls={
        'Source': 'https://github.com/arrrlo/CRO-Tax-Deptors',
    },
)

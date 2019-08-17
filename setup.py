from setuptools import setup, find_packages

with open('README.rst', encoding = 'UTF-8') as f:
    readme = f.read()

setup(
        name = '',
        version='0.1.0',
        description='',
        long_description= readme,
        author= 'Dylan',
        author_email='dylanf230@gmail.com',
        packages = find_packages('src'),
        package_dir={'': 'src'},
)

from setuptools import setup, find_packages

version = '0.8'

LONG_DESCRIPTION = """
"""

setup(
    name='django-lb-attachments',
    version=version,
    description="A django app to manager attachments.",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='attachment,django',
    author='vicalloy',
    author_email='zbirder@gmail.com',
    url='https://github.com/vicalloy/django-lb-attachments/',
    license='BSD',
    packages=find_packages(),
    package_data = {
        'attachments': [
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

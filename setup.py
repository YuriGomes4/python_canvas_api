from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='py_canvas',
    version='0.0.1',
    license='MIT License',
    author='Yuri Gomes',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='yurialdegomes@gmail.com',
    keywords='canvas lms',
    description=u'Wrapper não oficial do Canvas LMS',
    packages=['py_canvas'],
    install_requires=['requests'],)
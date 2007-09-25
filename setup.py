from setuptools import setup, find_packages

name = "plone.recipe.command"
setup(
    name = name,
    version = "1.1.1",
    author = "Daniel Chapelle",
    author_email = "daniel@bubblenet.be",
    description = "Execute arbitrary commands through os.system",
    license = "GPL",
    keywords = "buildout",
    classifiers = [
        "Framework :: Buildout",
    ],
    url='http://www.python.org/pypi/'+name,

    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires = ['zc.buildout', 'setuptools'],
    entry_points = {'zc.buildout':
                    ['default = %s:Recipe' % name]},
    )

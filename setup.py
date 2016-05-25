import glob
import os
from setuptools import setup


# get all of the scripts
scripts = glob.glob("bin/*")

# read in the description from README
with open("README.md") as stream:
    long_description = stream.read()

github_url='https://github.com/deanmalmgren/trello-todoist'

# read in the dependencies from the virtualenv requirements file
dependencies, dependency_links = [], []
filename = os.path.join("REQUIREMENTS")
with open(filename, 'r') as stream:
    for line in stream:
        line = line.strip()
        if line.startswith("http"):
            dependency_links.append(line)
        else:
            package = line.split('#')[0]
            if package:
                dependencies.append(package)


setup(
    name='trello-todoist',
    version='0.1.0',
    description="convert due trello cards to todoist tasks",
    long_description=long_description,
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Dean Malmgren',
    author_email='dean.malmgren@datascopeanalytics.com',
    license='MIT',
    scripts=scripts,
    install_requires=dependencies,
    dependency_links=dependency_links,
    zip_safe=False,
)

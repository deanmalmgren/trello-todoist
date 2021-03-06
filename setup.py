import glob
import os
from setuptools import setup

# get all of the scripts
this_dir = os.path.dirname(os.path.abspath(__file__))
scripts = glob.glob(os.path.join(this_dir, "bin", "*"))

# read in the description from README
with open("README.md") as stream:
    long_description = stream.read()

github_url='https://github.com/deanmalmgren/trello-todoist'

# read in the dependencies from the virtualenv requirements file
dependencies, dependency_links = [], []
filename = os.path.join(this_dir, "requirements", "python")
with open(filename, 'r') as stream:
    for line in stream:
        line = line.strip()
        if line.startswith("http"):
            dependency_links.append(line)
        else:
            package = line.split('#')[0]
            if package:
                dependencies.append(package)

# create the package
setup(
    name='trello-todoist',
    version='0.2.0',
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

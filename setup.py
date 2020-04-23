import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'EOEPCA-PyLibraryTemplate',                        # How you named your package folder (MyLibrary)
  version = '0.0.1',                                        # Start with a small number and increase it with every change you make
  author = 'EOEPCA',
  author_email = 'angel.lozano@deimos-space.com',           # Your email, which must be registered in PyPi's EOEPCA organization
  description = 'Dummy example for UM PyLibrary Template',  # Give a short description about your library
  long_description = long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/EOEPCA/um-pylibrary-template',  # Provide the link to the github
  packages=setuptools.find_packages(),
  license='apache-2.0',                                     # Do NOT change this unless you know what you are doing
  keywords = ['Dummy', 'Template', 'User', 'Management'],   # Keywords that define your package best, in order to find it on a search
  classifiers=[
    'Development Status :: 3 - Alpha',                      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
  ],
  python_requires='>=3.6',
)

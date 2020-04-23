<!--
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** um-pylibrary-template, PyLibraryTemplate
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
![Build][build-shield]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EOEPCA/um-pylibrary-template">
  </a>

  <h3 align="center">PyLibraryTemplate</h3>

  <p align="center">
    Template for developing an EOEPCA Library
    <br />
    <a href="https://github.com/EOEPCA/um-pylibrary-template"><strong>Explore the docs</strong></a>
    .
    <a href="https://github.com/EOEPCA/um-pylibrary-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/EOEPCA/um-pylibrary-template/issues">Request Feature</a>
  </p>
</p>

## Setup this template!
- Edit setup.py to fit your repository
- Replace code and requirements.txt in src by your own! Make sure to use pytest, or replace it in the .travis.yml to use the correct testing suite 
- Generate a new token in PyPi account exclusively for this library

- setup the following variables (in travis webpage, for this project) to ensure travis automated CI works (https://travis-ci.com/github/EOEPCA/<project>/settings):
    1. GH_REPOS_NAME (this repo's name)
    2. GH_USER_NAME (GitHub name for the responsible of this module)
    3. GH_USER_EMAIL (GitHub email for the responsible of this module)
    4. TOKEN_PYPI (Token you created in a previous step)

- Un-comment the "notifications" segment in .travis.yml, and input the correct data for slack and/or emails you want to notify

- Edit readme to fit your repository, deleting this part!

## Table of Contents

- [Setup this template!](#setup-this-template)
- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Testing](#testing)
- [Documentation & Usage](#documentation--usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## About The Project

### Built With

- [Python](https://www.python.org//)
- [PyTest](https://docs.pytest.org)
- [YAML](https://yaml.org/)
- [Travis CI](https://travis-ci.com/)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- [Python 3](https://www.python.org//)
- [Pip](https://pip.pypa.io/en/stable/)

### Installation

Just download the library using pip

```sh
pip install PyLibraryTemplate
```

### Testing

```sh
pytest PyLibraryTemplate/tests
```

## Documentation & Usage

The component documentation can be found at https://eoepca.github.io/um-pylibrary-template/.

## Roadmap

See the [open issues](https://github.com/EOEPCA/um-pylibrary-template/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the Apache-2.0 License. See `LICENSE` for more information.

## Contact

[EOEPCA mailbox](eoepca.systemteam@telespazio.com)

Project Link: [https://github.com/EOEPCA/um-pylibrary-template](https://github.com/EOEPCA/um-pylibrary-template)

## Acknowledgements

- README.md is based on [this template](https://github.com/othneildrew/Best-README-Template) by [Othneil Drew](https://github.com/othneildrew).


[contributors-shield]: https://img.shields.io/github/contributors/EOEPCA/um-pylibrary-template.svg?style=flat-square
[contributors-url]: https://github.com/EOEPCA/um-pylibrary-template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EOEPCA/um-pylibrary-template.svg?style=flat-square
[forks-url]: https://github.com/EOEPCA/um-pylibrary-template/network/members
[stars-shield]: https://img.shields.io/github/stars/EOEPCA/um-pylibrary-template.svg?style=flat-square
[stars-url]: https://github.com/EOEPCA/um-pylibrary-template/stargazers
[issues-shield]: https://img.shields.io/github/issues/EOEPCA/um-pylibrary-template.svg?style=flat-square
[issues-url]: https://github.com/EOEPCA/um-pylibrary-template/issues
[license-shield]: https://img.shields.io/github/license/EOEPCA/um-pylibrary-template.svg?style=flat-square
[license-url]: https://github.com/EOEPCA/um-pylibrary-template/blob/master/LICENSE
[build-shield]: https://www.travis-ci.com/EOEPCA/um-pylibrary-template.svg?branch=master

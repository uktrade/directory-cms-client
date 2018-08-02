# directory-cms-client

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![snyk-image]][snyk]

**Directory CMS client.**

Client for the Directory Content Management read-only API.
---

## Installation

```sh
    $ pip install directory-cms-client
```

The api client expects the following settings:

| Setting                                  | Notes                                                       |
| ---------------------------------------- | ----------------------------------------------------------- |
| DIRECTORY_CMS_API_CLIENT_BASE_URL        |                                                             |
| DIRECTORY_CMS_API_CLIENT_API_KEY         | Unique to client. Retrieved during the on-boarding process. |
| DIRECTORY_CMS_API_CLIENT_SENDER_ID       | Unique to client. Retrieved during the on-boarding process. |
| DIRECTORY_CMS_API_CLIENT_DEFAULT_TIMEOUT |                                                             |

Once that is done the API client can be used:

```py
from directory_api_client.client import cms_api_client
```

## Development

```shell
$ git clone https://github.com/uktrade/directory-cms-client
$ cd directory-cms-client
$ [create virtual environment and activate]
$ pip install -r requirements_test.txt
```

## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                     |
| --------------------------- |
| DIRECTORY_PYPI_USERNAME     |
| DIRECTORY_PYPI_PASSWORD     |

Then run the following command:
```sh
    make publish
```

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-cms-client/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-cms-client/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-cms-client/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-cms-client

[pypi-image]: https://badge.fury.io/py/directory-cms-client.svg
[pypi]: https://badge.fury.io/py/directory-cms-client

[snyk-image]: https://snyk.io/test/github/uktrade/directory-cms-client/badge.svg
[snyk]: https://snyk.io/test/github/uktrade/directory-cms-client

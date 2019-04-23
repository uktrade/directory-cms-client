# directory-cms-client

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![pypi-image]][pypi]
[![semver-image]][semver]

**Directory CMS client.**

Client for the Directory Content Management read-only API.
---

## Installation

    $ pip install directory-cms-client

The api client expects the following settings:

| Setting                                  | Notes                                                       |
| -----------------------------------------| ----------------------------------------------------------- |
| DIRECTORY_CMS_API_CLIENT_BASE_URL        |                                                             |
| DIRECTORY_CMS_API_CLIENT_API_KEY         | Unique to client. Retrieved during the on-boarding process. |
| DIRECTORY_CMS_API_CLIENT_SENDER_ID       | Unique to client. Retrieved during the on-boarding process. |
| DIRECTORY_CMS_API_CLIENT_DEFAULT_TIMEOUT |                                                             |
| DIRECTORY_CMS_API_CLIENT_SERVICE_NAME    | Unique to client, can be hardcoded.                         |

The following [directory client core settings](https://github.com/uktrade/directory-client-core) also apply to directory cms client:

| Setting                                            | Notes                                                 |
| ---------------------------------------------------| ------------------------------------------------------|
| DIRECTORY_CLIENT_CORE_CACHE_EXPIRE_SECONDS         | Duration to store the retrieved content in the cache. |    |
| DIRECTORY_CLIENT_CORE_CACHE_LOG_THROTTLING_SECONDS | Duration to throttle log events for a given url for.  |

And also specify a cache with name `cms_fallback`:

```
CACHES = {
    'cms_fallback': ...
}
```

Once that is done the API client can be used:

```py
from directory_api_client.client import cms_api_client
```

## Development

```shell
$ git clone https://github.com/uktrade/directory-cms-client
$ cd directory-cms-client
$ [create virtual environment and activate]
$ make test_requirements
```

## Publish to PyPI

The package should be published to PyPI on merge to master. If you need to do it locally then get the credentials from rattic and add the environment variables to your host machine:

| Setting                     |
| --------------------------- |
| DIRECTORY_PYPI_USERNAME     |
| DIRECTORY_PYPI_PASSWORD     |

Then run the following command:

    $ make publish

[code-climate-image]: https://codeclimate.com/github/uktrade/directory-cms-client/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-cms-client

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-cms-client/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-cms-client/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-cms-client/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-cms-client

[pypi-image]: https://badge.fury.io/py/directory-cms-client.svg
[pypi]: https://badge.fury.io/py/directory-cms-client

[semver-image]: https://img.shields.io/badge/Versioning%20strategy-SemVer-5FBB1C.svg
[semver]: https://semver.org

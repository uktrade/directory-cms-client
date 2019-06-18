# Changelog

## [10.1.0](https://pypi.org/project/directory-cms-client/10.0.1/) (2019-05-31)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/46/files)

**Implemented enhancements:**

- Added `limit` and `offset` optional params to `list_by_page_type` to allow for pagination


## [10.0.1](https://pypi.org/project/directory-cms-client/10.0.1/) (2019-05-30)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/44/files)

**Implemented enhancements:**

- Upgraded directory client core to prevent cache from concluding uncached pages are cached


## [10.0.0](https://pypi.org/project/directory-cms-client/10.0.0/) (2019-04-23)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/43/files)

**Implemented enhancements:**

- Upgraded directory client core to reduce overzealous logging from the fallback cache.
- Improved documentation in readme

**Breaking changes:**

- Directory client core has been upgraded a major version 5.0.0. [See](https://github.com/uktrade/directory-client-core/pull/16)
- Dropped support for Python 3.5

## [9.0.0](https://pypi.org/project/directory-cms-client/9.0.0/) (2019-04-23)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/42/files)

**Implemented enhancements:**

- Removed lookup_by_full_path
- Added lookup_by_path

**Breaking changes:**

- Removed lookup_by_full_path


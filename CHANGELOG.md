# Changelog

## [12.0.0](https://pypi.org/project/directory-cms-client/12.0.0/) (2022-09-07)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/53/files)

**Implemented enhancements:**

- GLS-393 - Upgrade to be compatable with Django 3.2

## [11.1.1](https://pypi.org/project/directory-cms-client/11.1.1/) (2020-02-18)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/51/files)

**Implemented enhancements:**

- TT-2288 Added support for custom authenticators


## [11.1.0](https://pypi.org/project/directory-cms-client/11.0.0/) (2019-12-03)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/50/files)

**Implemented enhancements:**

- Added `lookup_country_guides` and `list_regions` methods


## [11.0.0](https://pypi.org/project/directory-cms-client/11.0.0/) (2019-09-23)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/49/files)

**Implemented enhancements:**

- Added `lookup_industries_by_tag` and `list_industry_tags` methods

**Breaking changes:**

- Removed `lookup_by_tag` method

## [10.2.0](https://pypi.org/project/directory-cms-client/10.2.0/) (2019-08-20)
[Full Changelog](https://github.com/uktrade/directory-cms-client/pull/48/files)

**Implemented enhancements:**

- Upgraded directory client core and test requirements

## [10.1.0](https://pypi.org/project/directory-cms-client/10.1.0/) (2019-06-18)
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

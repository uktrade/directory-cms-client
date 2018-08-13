import abc
from functools import wraps
import json
import logging
from urllib.parse import urlencode

from requests.exceptions import HTTPError, RequestException
from w3lib.url import canonicalize_url


logger = logging.getLogger(__name__)


MESSAGE_CACHE_HIT = 'CMS fallback cache hit. Displaying cached content.'
MESSAGE_CACHE_MISS = 'CMS fallback cache miss. Cannot display any content.'


class AbstractCMSResponse(abc.ABC):

    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code

    def raise_for_status(self):
        if not 200 <= self.status_code < 300:
            raise HTTPError(self.content)

    def json(self):
        return json.loads(self.content)

    @classmethod
    def from_response(cls, response):
        return cls(
            content=response.content,
            status_code=response.status_code,
        )


class CMSLiveResponse(AbstractCMSResponse):
    pass


class CMSCacheResponse(AbstractCMSResponse):
    pass


class CMSFailureResponse(AbstractCMSResponse):
    pass


def fallback(cache):
    def closure(func):
        @wraps(func)
        def wrapper(class_instance, url, params={}, *args, **kwargs):
            cache_key = canonicalize_url(url + '?' + urlencode(params))
            try:
                cms_response = func(
                    class_instance, url=url, params=params, *args, **kwargs
                )
                cms_response.raise_for_status()
            except RequestException:
                content = cache.get(cache_key)
                if content:
                    response = CMSCacheResponse(
                        content=content, status_code=200
                    )
                    logger.warn(
                        MESSAGE_CACHE_HIT,
                        extra={
                            'status_code': cms_response.status_code, 'url': url
                        }
                    )
                else:
                    response = CMSFailureResponse.from_response(cms_response)
                    logger.exception(
                        MESSAGE_CACHE_MISS,
                        extra={
                            'status_code': cms_response.status_code, 'url': url
                        }
                    )
            else:
                cache.set(cache_key, cms_response.content)
                response = CMSLiveResponse.from_response(cms_response)
            return response
        return wrapper
    return closure

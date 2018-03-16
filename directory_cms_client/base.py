import directory_client_core.base


class BaseAPIClient(directory_client_core.base.BaseAPIClient):
    endpoints = {
        'page': '/api/pages/{page_id}/',
        'pages': '/api/pages/',
    }

    def list_pages(
        self, page_type, fields=None, draft_token=None, language_code=None
    ):
        return self.get(
            url=self.endpoints['pages'],
            params={'fields': fields or ['*'], 'type': page_type},
            draft_token=draft_token,
            language_code=language_code
        )

    def get_page(self, page_id, draft_token=None, language_code=None):
        return self.get(
            url=self.endpoints['page'].format(page_id=page_id),
            draft_token=draft_token,
            language_code=language_code
        )

    def get(self, language_code, draft_token, params=None, *args, **kwargs):
        if params is None:
            params = {}
        if language_code:
            params['lang'] = language_code
        if draft_token:
            params['draft_token'] = draft_token
        return super().get(params=params, *args, **kwargs)

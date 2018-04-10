from directory_cms_client.base import BaseAPIClient

from directory_cms_client.find_a_supplier import FindASupplierClient
from directory_cms_client.export_readiness import ExportReadinessClient


class DirectoryCMSClient(BaseAPIClient):

    def __init__(self, base_url=None, api_key=None):
        super().__init__(base_url, api_key)
        self.find_a_supplier = FindASupplierClient(base_url, api_key)
        self.export_readiness = ExportReadinessClient(base_url, api_key)

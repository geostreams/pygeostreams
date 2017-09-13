"""
    Clowder Dataset API for GeoStreams
"""

import logging

from pygeotemporal.client import ClowderClient


class DatasetsApi(object):
    """
        API to manage the REST CRUD endpoints for datasets.
    """
    def __init__(self, client=None, host=None, key=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = ClowderClient(host=host, key=key, username=username, password=password)

    def datasets_get(self):
        """
        Get the list of all available datasets.

        :return: Full list of datasets.
        :rtype: `requests.Response`
        """
        logging.debug("Getting all datasets")
        try:
            return self.client.get("/datasets/")
        except Exception as e:
            logging.error("Error retrieving dataset list: %s", e.message)

    def dataset_get(self, dataset_id):
        """
        Get a specific dataset by id.

        :return: Sensor object as JSON.
        :rtype: `requests.Response`
        """
        logging.debug("Getting dataset %s" % dataset_id)
        try:
            return self.client.get("/datasets/%s" % dataset_id)
        except Exception as e:
            logging.error("Error retrieving dataset %s: %s" % (dataset_id, e.message))

    def create_empty(self, dataset_id):
        """
        Create dataset.

        :return: If successful or not.
        :rtype: `requests.Response`
        """
        logging.debug("Adding dataset")
        try:
            return self.client.post("/datasets/createempty", dataset_id)
        except Exception as e:
            logging.error("Error adding datapoint %s: %s" % (dataset_id, e.message))

    def dataset_delete(self, dataset_id):
        """
        Delete a specific dataset by id.

        :return: If successfull or not.
        :rtype: `requests.Response`
        """
        logging.debug("Deleting dataset %s" % dataset_id)
        try:
            return self.client.delete("/datasets/%s" % dataset_id)
        except Exception as e:
            logging.error("Error retrieving dataset %s: %s" % (dataset_id, e.message))

    def upload_file(self, dataset_id, file):
        """
        Add a file to a dataset.

        :return: If successfull or not.
        :rtype: `requests.Response`
        """
        logging.debug("Uploading a file to dataset %s" % dataset_id)
        try:
            return self.client.post_file("/uploadToDataset/%s" % dataset_id, file)
        except Exception as e:
            logging.error("Error upload to dataset %s: %s" % (dataset_id, e.message))

    def add_metadata(self, dataset_id, metadata):
        """
        Add a file to a dataset

        :return: If successfull or not.
        :rtype: `requests.Response`
        """

        logging.debug("Update metadata of dataset %s" % dataset_id)
        try:
            return self.client.post("/datasets/%s/metadata" % dataset_id, metadata)
        except Exception:
            logging.error("Error upload to dataset %s: %s" % (dataset_id, e.message))

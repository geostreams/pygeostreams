# coding: utf-8

"""
    Clowder Streams API
"""

from pyclowder.client import ClowderClient
import logging


class StreamsApi(object):

    def __init__(self, client=None, host=None, key=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = ClowderClient(host=host, key=key, username=username, password=password)

    def streams_get(self):
        """
        Get the list of all available streams.

        :return: Full list of sensors.
        :rtype: `requests.Response`
        """
        logging.debug("Getting all streams")
        try:
            return self.client.get("/geostreams/streams")
        except Exception as e:
            logging.error("Error retrieving sensor list: %s", e.message)

    def sensor_create_json(self, name, longitude, latitude, elevation, popupContent, region):
        """Create sensor definition in JSON"""
        sensor = {
            "name": name,
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    longitude,
                    latitude,
                    elevation
                ]
            },
            "properties": {
                "name": name,
                "popupContent": popupContent,
                "region": region
            }
        }
        return sensor

    def stream_post(self, stream):
        """
        Create stream.

        :return: If successful or not.
        :rtype: `requests.Response`
        """
        logging.debug("Adding stream")
        try:
            return self.client.post("/geostreams/streams", stream)
        except Exception as e:
            logging.error("Error adding datapoint %s" % stream, e.message)

    def stream_delete(self, stream_id):
        """
        Delete a specific stream by id.

        :return: If successfull or not.
        :rtype: `requests.Response`
        """
        logging.debug("Deleting stream %s" % stream_id)
        try:
            return self.client.delete("/geostreams/streams/%s" % stream_id)
        except Exception as e:
            logging.error("Error retrieving sensor %s" % stream_id, e.message)


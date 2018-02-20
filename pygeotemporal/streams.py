"""
    Clowder Streams API
"""

import logging

from pygeotemporal.client import ClowderClient


class StreamsApi(object):
    """
        API to manage the REST CRUD endpoints for Streams.
    """
    def __init__(self, client=None, host=None, key=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = ClowderClient(host=host, key=key, username=username, password=password)

    def streams_get(self):
        """
        Get the list of all available streams.

        :return: Full list of streams.
        :rtype: `requests.Response`
        """
        logging.debug("Getting all streams")
        try:
            return self.client.get("/geostreams/streams")
        except Exception as e:
            logging.error("Error retrieving stream list: %s", e.message)

    def stream_get_by_name_json(self, stream_name):
        """
        Get a specific stream by id.

        :return: stream object as JSON.
        :rtype: `requests.Response`
        """
        logging.debug("Getting stream %s" % stream_name)
        stream = self.client.get("/geostreams/streams?stream_name=" + stream_name).json()
        if 'status' in stream and stream['status'] == "No data found":
            return None
        else:
            return stream

    def stream_post(self, stream):
        """
        Create stream.

        :return: stream json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding stream")

        try:
            return self.client.post("/geostreams/streams", stream)
        except Exception as e:
            logging.error("Error retrieving stream %s: %s", stream_id, e.message)

    def stream_post_json(self, stream):
        """
        Create stream.

        :return: stream json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding or getting stream")

        stream_from_clowder = self.stream_get_by_name_json(stream['name'])

        if stream_from_clowder is None:
            logging.info("Creating stream with name: " + stream['name'])
            stream_from_clowder = self.client.post("/geostreams/streams", stream)
            return stream_from_clowder.json()

        else:
            logging.info("Found stream %s", stream['name'])
            return stream_from_clowder[0]

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
            logging.error("Error deleting stream %s: %s", stream_id, e.message)

    def stream_create_json_from_sensor(self, sensor):
        """
        Create stream from sensor. Note: It does not post the stream to the API

        :param: sensor
        :return: stream Json object
        """
        stream = {
            "sensor_id": str(sensor["id"]),
            "name": sensor["name"],
            "type": sensor["type"],
            "geometry": sensor["geometry"],
            "properties": sensor["properties"]
        }

        return stream

    def stream_delete_range(self, start, end):
        """
        Deletes streams in a range of indexes [start, end]

        """
        for i in range(start, end + 1):
            self.stream_delete(i)
        return

"""
    Clowder Sensors API.
"""

import logging
import time

from pygeotemporal.client import ClowderClient


class SensorsApi(object):
    """
        API to manage the REST CRUD endpoints for sensors.
    """
    def __init__(self, client=None, host=None, key=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = ClowderClient(host=host, key=key, username=username, password=password)

    def sensors_get(self):
        """
        Get the list of all available sensors.

        :return: Full list of sensors.
        :rtype: `requests.Response`
        """
        logging.debug("Getting all sensors")
        try:
            return self.client.get("/geostreams/sensors")
        except Exception as e:
            logging.error("Error retrieving sensor list: %s", e.message)

    def sensors_refresh(self):
        """
        Get all available sensors one by one, return nothing

        :rtype: `requests.Response`
        """
        logging.debug("Getting all sensorsby each id")
        try:
            sensorList = self.client.get("/geostreams/sensors")

            for sensor in sensorList.json():
                logging.debug("refresh sensor %s", sensor['id'])
                self.client.get("/geostreams/sensors/%s" % sensor['id'])
                binningfilter = 'smart'
                if sensor['properties']['type']['id'] == 'epa': 
                    binningfilter = 'semi'

                self.client.get("/geostreams/datapoints/bin/%s/1?sensor_id=%s" % (binningfilter, sensor['id']))
                time.sleep(100)     
            return True    
        except Exception as e:
            logging.error("Error retrieving sensor list: %s", e.message)

    def sensor_get(self, sensor_id):
        """
        Get a specific sensor by id.

        :return: Sensor object as JSON.
        :rtype: `requests.Response`
        """
        logging.debug("Getting sensor %s" % sensor_id)
        try:
            return self.client.get("/geostreams/sensors/%s" % sensor_id)
        except Exception as e:
            logging.error("Error retrieving sensor %s: %s", sensor_id, e.message)

    def sensor_get_by_name(self, sensor_name):
        """
        Get a specific sensor by id.

        :return: Sensor object as JSON.
        :rtype: `requests.Response`
        """
        logging.debug("Getting sensor %s" % sensor_name)
        try:
            return self.client.get("/geostreams/sensors?sensor_name=" + sensor_name)
        except Exception as e:
            logging.error("Error retrieving sensor %s: %s", sensor_name, e.message)
            return None

    def sensor_post(self, sensor):
        """
        Create sensor.

        :return: sensor json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding sensor")
        try:
            return self.client.post("/geostreams/sensors", sensor)
        except Exception as e:
            logging.error("Error adding sensor %s: %s", sensor['name'], e.message)

    def sensor_post_json(self, sensor):
        """
        Create sensor.

        :return: sensor json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding or getting sensor")
        try:
            sensor_from_clowder = self.sensor_get_by_name(sensor['name']).json()
            if not sensor_from_clowder:
                logging.info("Creating sensor with name: " + sensor['name'])
                sensor_from_clowder = self.client.post("/geostreams/sensors", sensor)
                return sensor_from_clowder.json()

            else:
                logging.info("Found sensor " + sensor['name'])
                return sensor_from_clowder[0]
        except Exception as e:
            logging.error("Error adding sensor %s: %s", sensor['name'], e.message)

    def sensor_delete(self, sensor_id):
        """
        Delete a specific sensor by id.

        :return: If successfull or not.
        :rtype: `requests.Response`
        """
        logging.debug("Deleting sensor %s" % sensor_id)
        try:
            return self.client.delete("/geostreams/sensors/%s" % sensor_id)
        except Exception as e:
            logging.error("Error retrieving sensor %s: %s", sensor_id, e.message)

    def sensor_create_json(self, name, longitude, latitude, elevation, popupContent, region, huc=None, network=None,
                           id=None, title=None):
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
        if huc:
            sensor["properties"]["huc"] = huc
        if network or id or title:
            sensor['properties']['type'] = {}
            if network:
                sensor['properties']['type']['network'] = network
            if id:
                sensor['properties']['type']['id'] = id
            if title:
                sensor['properties']['type']['title'] = title
        return sensor

    def sensor_statistics_post(self, sensor_id):
        """
        Update sensor statistics.

        :return: Full list of sensors.
        :rtype: `requests.Response`
        """
        logging.debug("Updating sensor statistics")
        try:
            # TODO this should be a PUT on the API side, not a GET
            return self.client.get_auth("/geostreams/sensors/%s/update" % sensor_id)
        except Exception as e:
            logging.error("Error updating sensor statistics for sensor %s: %s", sensor_id, e.message)

    def sensor_get_huc(self, latitude, longitude):
        huc_url = "http://gltg.ncsa.illinois.edu/api/huc?lat=" + str(latitude) + "&lng=" + str(longitude)
        huc_data = self.client.get_json(huc_url)
        return huc_data

import logging
import time
from typing import Union, Tuple
from pygeostreams.client import GeostreamsClient


class ParametersAPI(object):
    """
        API to manage the REST CRUD endpoints for Parameters.
    """

    def __init__(self, client=None, host=None, username=None, password=None):
        """Set client if provided otherwise create new one"""
        if client:
            self.api_client = client
        else:
            self.client = GeostreamsClient(host=host, username=username, password=password)

    def parameters_get(self, timeout: Union[int, Tuple[int, int]] = (125, 605)):
        """
        Get the list of all available parameters.

        :param timeout: Number of seconds Requests will wait to establish a connection.
        Specify a Tuple if connect and read timeouts should be different (with the first element being
        the connection timeout, and the second being the read timeout.
        :return: Full list of parameters.
        :rtype: `requests.Response`
        """
        logging.debug("Getting all parameters")
        try:
            return self.client.get("/parameters", timeout)
        except RequestException as e:
            logging.error(f"Error retrieving parameter list: {e}")
            raise e

    def parameter_create_json(self, parameter_name, parameter_title, parameter_unit, categories, search_view=True, explore_view=True,
                              scale_names=None, scale_colors=None):
        """
        Create a json definition for parameters

        :param categories: List of categories in format [[category_name,category_detail_type]...]
        :return: return JSON  that could be used in function parameter_post

        """
        data = {
            "parameter":
                {
                    "name": parameter_name,
                    "title": parameter_title,
                    "unit": parameter_unit,
                    "search_view": search_view,
                    "explore_view": explore_view,
                    "scale_names": scale_names,
                    "scale_colors": scale_colors
                },
            "categories": []
        }
        for category in categories:
            data["categories"].append({"name": category[0], "detail_type": category[1]})

        return data

    def parameter_post(self, parameter, timeout: Union[int, Tuple[int, int]] = (125, 605)):
        """
        Create parameter.

        :param parameter: parameter json
        :param timeout: Number of seconds Requests will wait to establish a connection.
        Specify a Tuple if connect and read timeouts should be different (with the first element being
        the connection timeout, and the second being the read timeout.
        :return: parameter json.
        :rtype: `requests.Response`
        """
        logging.debug("Adding parameter")
        try:
            return self.client.post("/parameters", parameter, timeout)
        except RequestException as e:
            logging.error(f"Error adding parameter {parameter['name']}: {e}")
            raise e

    def parameter_delete(self, parameter_id, timeout: Union[int, Tuple[int, int]] = (125, 605)):
        """
        Delete a specific parameter by id.

        :param parameter_id:
        :param timeout: Number of seconds Requests will wait to establish a connection.
        Specify a Tuple if connect and read timeouts should be different (with the first element being
        the connection timeout, and the second being the read timeout.
        :return: If successful or not.
        :rtype: `requests.Response`
        """
        logging.debug(f"Deleting parameter {parameter_id}")
        try:
            return self.client.delete("/parameters/%s" % parameter_id, timeout)
        except RequestException as e:
            logging.error(f"Error deleting parameter {parameter_id}: {e}")
            raise e

    def parameter_delete_by_name(self, parameter_name, timeout: Union[int, Tuple[int, int]] = (125, 605)):
        """
        Delete a specific parameter by name.

        :param parameter_name:
        :param timeout: Number of seconds Requests will wait to establish a connection.
        Specify a Tuple if connect and read timeouts should be different (with the first element being
        the connection timeout, and the second being the read timeout.
        :return: If successful or not.
        :rtype: `requests.Response`
        """

        logging.debug(f"Deleting parameter named {parameter_name}")
        try:
            return self.client.delete("/parameters/name/%s" % parameter_name, timeout)
        except RequestException as e:
            logging.error(f"Error deleting parameter named {parameter_name}: {e}")
            raise e

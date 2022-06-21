# Pygeostreams


Pygeostreams is a library that makes it easier to interact with
[GeoTemporal API v2](https://opensource.ncsa.illinois.edu/bitbucket/projects/GEOD/repos/geo-temporal-api-v2) and
[Clowder](https://opensource.ncsa.illinois.edu/bitbucket/projects/CATS/repos/clowder)
to create sensors, , parameters and datapoints.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pygeostreams.

```bash
pip install pygeostreams
```

## Usage

```python
# Import different classes to use different Geostream APIs  
from pygeostreams.client import GeostreamsClient
from pygeostreams.datapoints import DatapointsApi
from pygeostreams.sensors import SensorsApi
from pygeostreams.streams import StreamsApi
from pygeostreams.parameters import ParametersAPI

# returns 'words'
foobar.pluralize('word')

# Create a new sensor
sensors_client = SensorsApi(host='https://example.com', username='username@example.com', password='example')
sensor_json = sensors_client.sensor_create_json("Site Name",
                                                  longitude = 0.000,
                                                  latitude= 0.000,
                                                  elevation= 0,
                                                  organization_id='Organization ID',
                                                  title="Title")


sensor = sensors_client.sensor_post(sensor_json)

# Create a new parameters 
client = ParametersAPI(host='https://example.com', username='username@example.com', password='example')
parameter_json = client.parameter_create_json('soil_temperature_100cm', 'Soil Temperature at 100 cm', 'C', categories=[['Soil', 'time']])
```


Example parsers can be found at [Seagrant GLFMSP Parsers](https://opensource.ncsa.illinois.edu/bitbucket/projects/GEOD/repos/seagrant-parsers-py/browse/GLFMSP/glfmsp-2017.py)




## License

This software is licensed under the [NCSA Open Source license](https://opensource.org/licenses/NCSA), an open source license [based on the MIT/X11 license and the 3-clause BSD license.](https://en.wikipedia.org/wiki/University_of_Illinois/NCSA_Open_Source_License)


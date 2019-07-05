# System
import json

# Third Party
from flask import Flask, json
from flask_cors import CORS

# Local
from x_com import count_rows_in_table, unique_ship_shapes, evac_priorties, closest_to_area_52

app = Flask(__name__)
CORS(app)

@app.route('/total_sightings', methods=['GET'])
def counter_endpoint( event=None, context=None ):
    """
    API endpoint that returns the total number of UFO sightings.

    An example request might look like:

    .. sourcecode:: http

       GET www.x.com/counter HTTP/1.1
       Host: example.com
       Accept: application/json, text/javascript

    Results will be returned as JSON object with the following format:

    .. code-block:: json

        {
          "count": <number>
        }

    """

    return app.response_class( json.dumps( count_rows_in_table() ), mimetype='application/json' )

@app.route('/unique_ship_shapes', methods=['GET'])
def unique_ship_shapes_endpoint( event=None, context=None ):
    """
    API endpoint that returns the total number of unique shapes of alien ships across all sightings.

    An example request might look like:

    .. sourcecode:: http

       GET www.x.com/unique_ship_shapes HTTP/1.1
       Host: example.com
       Accept: application/json, text/javascript

    Results will be returned as JSON object with the following format:

    .. code-block:: json

        {
          "count": <number>
        }

    """

    return app.response_class( json.dumps( unique_ship_shapes() ), mimetype='application/json' )

@app.route('/evac_priorties', methods=['GET'])
def evac_priorties_endpoint( event=None, context=None ):
    """
    API endpoint that returns Top-10 Cities in the United States with the most UFO sightings in descending order.

    An example request might look like:

    .. sourcecode:: http

       GET www.x.com/evac_priorties HTTP/1.1
       Host: example.com
       Accept: application/json, text/javascript

    Results will be returned as JSON object with the following format:

    .. code-block:: json

        {
          "sightings": [
            {
                "city": <city_name_with_most_sightings:string>,
                "count": <sightings_in_this_city:int>
            },
            {
                "city": <city_name_with_second_most_sightings:string>,
                "count": <sightings_in_this_city:int>
            },
            ...
            ...
            {
                "city": <city_name_with_tenth_most_sightings:string>,
                "count": <sightings_in_this_city:int>
            }
          ]
        }
    """

    return app.response_class( json.dumps( evac_priorties() ), mimetype='application/json' )

@app.route('/closest_to_area_52', methods=['GET'])
def closest_to_area_52_endpoint( event=None, context=None ):
    """
    API endpoint that returns information about UFO sightings closest to Area 52.

    An example request might look like:

    .. sourcecode:: http

       GET www.x.com/closest_to_area_52_endpoint HTTP/1.1
       Host: example.com
       Accept: application/json, text/javascript

    Results will be returned as JSON object with the following format:

    .. code-block:: json

        {
          "sightings": [
            {
                "city": <city_closest_to_base:string>,
                "country": <country_of_city:string>,
                ...
                ...
                "shape": <shape_of_ufo:string>,
                "distance": <distance_of_ufo_from_area52:float>
            },
            {
                "city": <city_second_closest:string>,
                "country": <country_of_city:string>,
                ...
                ...
                "shape": <shape_of_ufo:string>,
                "distance": <distance_of_ufo_from_area52:float>
            },
            {
                "city": <city_third_closest:string>,
                "country": <country_of_city:string>,
                ...
                ...
                "shape": <shape_of_ufo:string>,
                "distance": <distance_of_ufo_from_area52:float>
            }
          ]
        }
    """

    return app.response_class( json.dumps( closest_to_area_52() ), mimetype='application/json' )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

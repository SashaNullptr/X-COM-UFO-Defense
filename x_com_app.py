# System
import os
import json
import logging
from urllib import parse

# Third Party
from flask import Flask, request, json, redirect, url_for, send_from_directory
from flask_cors import CORS, cross_origin

# Local
from x_com import count_rows_in_table, unique_ship_shapes

app = Flask(__name__)
CORS(app)

@app.route('/counter', methods=['GET'])
def get_answer( event=None, context=None ):
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
def get_answer( event=None, context=None ):
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

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')

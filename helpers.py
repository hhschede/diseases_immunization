

# Extract values for Mapping (GeoJSON)
def extract_json_html(html):

    """function returns JSON object from raw string found on GitHub
    html input leads to raw file. input as string"""

    import requests
    import io
    import json

    pull = requests.get(html).content
    geojson = io.StringIO(pull.decode('utf-8')).getvalue()
    data = json.loads(geojson)

    return data


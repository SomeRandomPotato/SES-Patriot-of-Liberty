from urllib.request import urlopen
import json


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


url = ("https://api-hellhub-collective.koyeb.app/api/assignments")
page = (get_jsonparsed_data(url))
data = str(page['data'])
briefing = data[data.find('\'briefing\':')+12:data.find('\'', data.find('description\': ') - 1)]
print(briefing)

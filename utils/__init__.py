
import json
from django.core import serializers


def res_data(obj):
    return obj['fields']


def query_set_to_dir(query_set):
    data = json.loads(serializers.serialize('json', query_set))
    data_dir = list(map(res_data, data))
    return data_dir

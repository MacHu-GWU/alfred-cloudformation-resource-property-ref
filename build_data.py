# -*- coding: utf-8 -*-

"""
The purpose of this script is to inspect the data schema, data value of the
json file download from https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

I have to deeply understand the data in spec file, so I can generate cottonformation
code out of it.
"""

import os
import json
import requests

HOME = os.path.expanduser("~")
HERE = os.path.dirname(os.path.abspath(__file__))
SPEC_FILE = os.path.join(HERE, "spec.json")
FTS_DATA_FILE = os.path.join(HOME, ".alfred-fts", "cloudformation.json")
FTS_SETTING_FILE = os.path.join(HOME, ".alfred-fts", "cloudformation-setting.json")


def write_file(path, text):
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))


def download_spec_file():
    if not os.path.exists(SPEC_FILE):
        url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
        response = requests.get(url)
        with open(SPEC_FILE, "wb") as f:
            f.write(response.content)


def read_spec_file():
    with open(SPEC_FILE, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    return data


alfred_settings_data = {
    "columns": [
        {
            "name": "title",
            "ngram_maxsize": 10,
            "ngram_minsize": 2,
            "type_is_ngram": True
        },
        {
            "name": "subtitle",
            "type_is_store": True
        },
        {
            "name": "arg",
            "type_is_store": True
        }
    ],
    "title_field": "{title}",
    "subtitle_field": "{subtitle}",
    "arg_field": "{arg}",
    "autocomplete_field": "{title}",
}


def create_alfred_cloudformation_data_file():
    """
    Generate data file for alfred full text search anything:

    https://github.com/MacHu-GWU/afwf_fts_anything-project
    """
    spec_data = read_spec_file()

    alfred_data = list()

    for res_id, res_dct in spec_data["ResourceTypes"].items():
        if "Documentation" not in res_dct:
            continue
        print("Build {}".format(res_id))
        _, service, resource = res_id.split("::")
        doc_link = res_dct["Documentation"]
        dct = dict(
            title=f"Resource: {service} | {resource}",
            subtitle=f"open {doc_link}",
            arg=doc_link,
        )
        alfred_data.append(dct)

    for prop_id, prop_dct in spec_data["PropertyTypes"].items():
        if "Documentation" not in prop_dct:
            continue
        if prop_id == "Tag":
            continue
        _, service, prop_full_name = prop_id.split("::")
        resource, prop_name = prop_full_name.split(".")

        doc_link = prop_dct["Documentation"]
        dct = dict(
            title=f"Property: {service} | {resource} - {prop_name}",
            subtitle=f"open {doc_link}",
            arg=doc_link,
        )
        alfred_data.append(dct)

    write_file(FTS_DATA_FILE, json.dumps(alfred_data, indent=4))
    write_file(FTS_SETTING_FILE, json.dumps(alfred_settings_data, indent=4))


if __name__ == "__main__":
    download_spec_file()
    create_alfred_cloudformation_data_file()

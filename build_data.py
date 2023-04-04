# -*- coding: utf-8 -*-

"""
The purpose of this script is to inspect the data schema, data value of the
json file download from https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

I have to deeply understand the data in spec file, so I can generate cottonformation
code out of it.
"""

import json
import requests
from pathlib_mate import Path

dir_home = Path.home()
dir_here = Path.cwd().absolute()
path_spec_file = Path(dir_here, "spec.json")
p_alfred_data = Path(dir_here, f"cloudformation-data.json")
p_alfred_setting = Path(dir_here, f"cloudformation-setting.json")


def download_spec_file():
    if not path_spec_file.exists():
        url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
        response = requests.get(url)
        path_spec_file.write_bytes(response.content)


def read_spec_file():
    return json.loads(path_spec_file.read_text())


alfred_settings_data = {
    "fields": [
        {
            "name": "title_ngram",
            "type_is_store": True,
            "type_is_ngram": True,
            "ngram_maxsize": 10,
            "ngram_minsize": 2,
        },
        {
            "name": "title_phrase",
            "type_is_phrase": True,
            "weight": 2.0,
        },
        {
            "name": "url",
            "type_is_store": True,
        },
    ],
    "title_field": "{title_ngram}",
    "subtitle_field": "open {url}",
    "arg_field": "{url}",
    "autocomplete_field": "{title_ngram}",
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
        title = f"Resource: {service} | {resource}"
        dct = dict(
            title_ngram=title,
            title_phrase=title,
            url=doc_link,
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
        title = f"Property: {service} | {resource} - {prop_name}"
        dct = dict(
            title_ngram=title,
            title_phrase=title,
            url=doc_link,
        )
        alfred_data.append(dct)

    p_alfred_data.write_text(json.dumps(alfred_data, indent=4))
    p_alfred_setting.write_text(json.dumps(alfred_settings_data, indent=4))


if __name__ == "__main__":
    download_spec_file()
    create_alfred_cloudformation_data_file()

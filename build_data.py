# -*- coding: utf-8 -*-

"""
The purpose of this script is to inspect the data schema, data value of the
json file download from https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html

I have to deeply understand the data in spec file, so I can generate cottonformation
code out of it.
"""

from pathlib_mate import Path
import json
import requests

dir_home = Path.home()
dir_here = Path.cwd().absolute()
path_spec_file = Path(dir_here, "spec.json")
p_alfred_data = Path(dir_here, f"cloudformation.json")
p_alfred_setting_data = Path(dir_here, f"cloudformation-setting.json")


def download_spec_file():
    if not path_spec_file.exists():
        url = "https://d1uauaxba7bl26.cloudfront.net/latest/gzip/CloudFormationResourceSpecification.json"
        response = requests.get(url)
        path_spec_file.write_bytes(response.content)


def read_spec_file():
    return json.loads(path_spec_file.read_text())


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
        },
        {
            "name": "autocomplete",
            "type_is_store": True
        }
    ],
    "title_field": "{title}",
    "subtitle_field": "{subtitle}",
    "arg_field": "{arg}",
    "autocomplete_field": "{autocomplete}",
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
            auto_complete=f"Resource {service} {resource}",
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
            auto_complete=f"Property {service} {resource} {prop_name}",
        )
        alfred_data.append(dct)

    p_alfred_data.write_text(json.dumps(alfred_data, indent=4))
    p_alfred_setting_data.write_text(json.dumps(alfred_settings_data, indent=4))


if __name__ == "__main__":
    download_spec_file()
    create_alfred_cloudformation_data_file()

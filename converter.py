import bs4
import json
from pathlib_mate import PathCls as Path

doc_source_dir = Path("/Users/sanhehu/Downloads/aws-cloudformation-user-guide-master/doc_source")
resources_data = list()

RESOURCE_PATTERN = "aws-resource"
PROPERTY_PATTERN = "aws-properties"

for p in doc_source_dir.select_file():
    flag = False
    if p.fname.startswith(RESOURCE_PATTERN):
        entity_type = "Resource"
        fname_prefix = RESOURCE_PATTERN
        flag = True
    elif p.fname.startswith(PROPERTY_PATTERN):
        entity_type = "Property"
        fname_prefix = PROPERTY_PATTERN
        flag = True
    if flag:
        entity = p.fname.replace(fname_prefix+"-", "").replace("-", " ").title()
        title = "{}: {}".format(entity_type, entity)
        url = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/{}.html".format(p.fname)
        subtitle = "Open {}".format(url)
        arg = url
        dct = dict(title=title, subtitle=subtitle, arg=arg)
        resources_data.append(dct)
with open("ref.json", "wb") as f:
    f.write(json.dumps(resources_data, indent=4, sort_keys=True).encode("utf-8"))
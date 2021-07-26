CloudFormation Document Quick Search
==============================================================================

I create an `Alfred Workflow <https://www.alfredapp.com/workflows/>`_ framework called `Full Text Search Anything <https://github.com/MacHu-GWU/afwf_fts_anything-project>`_. You can bring your own json data, define how you gonna index it, then use Alfred Workflow to search it.

You can also download the dataset directly from `Release <https://github.com/MacHu-GWU/alfred-cloudformation-resource-property-ref/releases>`_. Just Download ``cloudformation-full-text-search-data.zip``, extract it in ``${HOME}/.alfred-fts``. Follow Alfred Workflow Config instruction in https://github.com/MacHu-GWU/afwf_fts_anything-project


How to Build Cloudformation full text search data
------------------------------------------------------------------------------

The idea is to use get list of document and url from AWS Docs https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html. And then use the full text search framework I created https://github.com/MacHu-GWU/afwf_fts_anything-project to search it in Alfred.

The ``build_data.py`` script can do the above automatically.

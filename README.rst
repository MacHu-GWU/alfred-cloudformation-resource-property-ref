CloudFormation Document Quick Search
==============================================================================


What is this?
------------------------------------------------------------------------------
I create an `Alfred Workflow <https://www.alfredapp.com/workflows/>`_ framework called `Full Text Search Anything <https://github.com/MacHu-GWU/afwf_fts_anything-project>`_. You can bring your own json data, define how you gonna index it, then use Alfred Workflow to search it.

**This project allows you to quickly search and browse** `AWS CloudFormation resource property reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_. It automates the creation of the "your own json data" for boto3 document searching.


How it Work?
------------------------------------------------------------------------------
The idea is to use get list of document and url from AWS Docs https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification.html. And then use the full text search framework I created https://github.com/MacHu-GWU/afwf_fts_anything-project to search it in Alfred.

Just run the following script, it will generate the data file and setting file on Git repo root directory.

.. code-block:: bash

    python3 build_data.py


How to Install?
------------------------------------------------------------------------------
**The automate way**:

    We have a `installation script <./install.py>`_, so just do:

    .. code-block:: bash

        python3 -c "$(curl -fsSL https://raw.githubusercontent.com/MacHu-GWU/alfred-cloudformation-resource-property-ref/master/install.py)"

**The manual way**:

    You can also download the dataset directly from `Release <https://github.com/MacHu-GWU/alfred-cloudformation-resource-property-ref/releases>`_. Just Download ``cloudformation-full-text-search-data.zip``, extract it in ``${HOME}/.alfred-fts``. Follow Alfred Workflow Config instruction in https://github.com/MacHu-GWU/afwf_fts_anything-project


I create an Alfred Workflow that allow me to search AWS CloudFormation Resource and Property Reference from anywhere in seconds.

The idea is to use get list of document and url from AWS Docs Github repo on https://github.com/awsdocs/aws-cloudformation-user-guide/tree/master/doc_source, extract the data put it in a json file. And then use the full text search framework I created https://github.com/MacHu-GWU/afwf_fts_anything-project to search it in Alfred.

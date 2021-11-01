#!/bin/env bash
npx @openapitools/openapi-generator-cli generate -i b2c2.yaml -g  python-legacy -o libs/python/b2c2_api --additional-properties=packageName=b2c2_api --additional-properties=projectName=b2c2_api

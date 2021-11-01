#!/bin/env bash
npx @openapitools/openapi-generator-cli generate -i b2c2.yaml -g typescript-axios -o libs/typescript/b2c2Api --additional-properties=npmName=b2c2-cli

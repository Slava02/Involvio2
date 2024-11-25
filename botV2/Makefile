.PHONY: generate-openapi
generate-openapi:
	@echo "Generating OpenAPI..."
	@curl http://localhost:8000/openapi-3.0.yaml > openapi.yaml

.PHONY: generate-python-sdk
generate-python-sdk:
	docker run --rm \
          -v ${PWD}:/local openapitools/openapi-generator-cli generate \
          -i /local/openapi.yaml \
          -g python \
          -o /local/clients/python \
          --additional-properties=packageName=random_coffe_client,projectName=random_coffe_client
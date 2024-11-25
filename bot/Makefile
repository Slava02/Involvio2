.PHONY: generate-openapi
generate-openapi:
	@echo "Generating OpenAPI..."
	@curl http://localhost:8000/openapi-3.0.yaml > clients/openapi-3.0.yaml

.PHONY: generate-go-sdk
generate-go-sdk:
	@echo "installing oapi-codegen..."
	@go install github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@latest
	@echo "Generating Go SDK..."
	@rm -rf sdk/sdk.go
	@oapi-codegen -generate "types,client" -package sdk clients/openapi-3.0.yaml > clients/sdk.go
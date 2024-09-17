// Code generated by go-swagger; DO NOT EDIT.

package spaces

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"net/http"

	"github.com/go-openapi/runtime"

	"github.com/Slava02/Involvio/internal/entity"
)

// GetSpaceOKCode is the HTTP code returned for type GetSpaceOK
const GetSpaceOKCode int = 200

/*
GetSpaceOK Successful operation

swagger:response getSpaceOK
*/
type GetSpaceOK struct {

	/*
	  In: Body
	*/
	Payload *entity.Space `json:"body,omitempty"`
}

// NewGetSpaceOK creates GetSpaceOK with default headers values
func NewGetSpaceOK() *GetSpaceOK {

	return &GetSpaceOK{}
}

// WithPayload adds the payload to the get space o k response
func (o *GetSpaceOK) WithPayload(payload *entity.Space) *GetSpaceOK {
	o.Payload = payload
	return o
}

// SetPayload sets the payload to the get space o k response
func (o *GetSpaceOK) SetPayload(payload *entity.Space) {
	o.Payload = payload
}

// WriteResponse to the client
func (o *GetSpaceOK) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.WriteHeader(200)
	if o.Payload != nil {
		payload := o.Payload
		if err := producer.Produce(rw, payload); err != nil {
			panic(err) // let the recovery middleware deal with this
		}
	}
}

// GetSpaceBadRequestCode is the HTTP code returned for type GetSpaceBadRequest
const GetSpaceBadRequestCode int = 400

/*
GetSpaceBadRequest Invalid data supplied

swagger:response getSpaceBadRequest
*/
type GetSpaceBadRequest struct {
}

// NewGetSpaceBadRequest creates GetSpaceBadRequest with default headers values
func NewGetSpaceBadRequest() *GetSpaceBadRequest {

	return &GetSpaceBadRequest{}
}

// WriteResponse to the client
func (o *GetSpaceBadRequest) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(400)
}

// GetSpaceNotFoundCode is the HTTP code returned for type GetSpaceNotFound
const GetSpaceNotFoundCode int = 404

/*
GetSpaceNotFound Space not found

swagger:response getSpaceNotFound
*/
type GetSpaceNotFound struct {
}

// NewGetSpaceNotFound creates GetSpaceNotFound with default headers values
func NewGetSpaceNotFound() *GetSpaceNotFound {

	return &GetSpaceNotFound{}
}

// WriteResponse to the client
func (o *GetSpaceNotFound) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(404)
}

// GetSpaceInternalServerErrorCode is the HTTP code returned for type GetSpaceInternalServerError
const GetSpaceInternalServerErrorCode int = 500

/*
GetSpaceInternalServerError Internal service error

swagger:response getSpaceInternalServerError
*/
type GetSpaceInternalServerError struct {
}

// NewGetSpaceInternalServerError creates GetSpaceInternalServerError with default headers values
func NewGetSpaceInternalServerError() *GetSpaceInternalServerError {

	return &GetSpaceInternalServerError{}
}

// WriteResponse to the client
func (o *GetSpaceInternalServerError) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(500)
}
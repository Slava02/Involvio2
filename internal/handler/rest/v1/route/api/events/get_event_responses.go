// Code generated by go-swagger; DO NOT EDIT.

package events

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"net/http"

	"github.com/go-openapi/runtime"

	"github.com/Slava02/Involvio/internal/entity"
)

// GetEventOKCode is the HTTP code returned for type GetEventOK
const GetEventOKCode int = 200

/*
GetEventOK successful operation

swagger:response getEventOK
*/
type GetEventOK struct {

	/*
	  In: Body
	*/
	Payload *entity.EventInfoResp `json:"body,omitempty"`
}

// NewGetEventOK creates GetEventOK with default headers values
func NewGetEventOK() *GetEventOK {

	return &GetEventOK{}
}

// WithPayload adds the payload to the get event o k response
func (o *GetEventOK) WithPayload(payload *entity.EventInfoResp) *GetEventOK {
	o.Payload = payload
	return o
}

// SetPayload sets the payload to the get event o k response
func (o *GetEventOK) SetPayload(payload *entity.EventInfoResp) {
	o.Payload = payload
}

// WriteResponse to the client
func (o *GetEventOK) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.WriteHeader(200)
	if o.Payload != nil {
		payload := o.Payload
		if err := producer.Produce(rw, payload); err != nil {
			panic(err) // let the recovery middleware deal with this
		}
	}
}

// GetEventBadRequestCode is the HTTP code returned for type GetEventBadRequest
const GetEventBadRequestCode int = 400

/*
GetEventBadRequest Invalid data supplied

swagger:response getEventBadRequest
*/
type GetEventBadRequest struct {
}

// NewGetEventBadRequest creates GetEventBadRequest with default headers values
func NewGetEventBadRequest() *GetEventBadRequest {

	return &GetEventBadRequest{}
}

// WriteResponse to the client
func (o *GetEventBadRequest) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(400)
}

// GetEventNotFoundCode is the HTTP code returned for type GetEventNotFound
const GetEventNotFoundCode int = 404

/*
GetEventNotFound Event not found

swagger:response getEventNotFound
*/
type GetEventNotFound struct {
}

// NewGetEventNotFound creates GetEventNotFound with default headers values
func NewGetEventNotFound() *GetEventNotFound {

	return &GetEventNotFound{}
}

// WriteResponse to the client
func (o *GetEventNotFound) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(404)
}

// GetEventInternalServerErrorCode is the HTTP code returned for type GetEventInternalServerError
const GetEventInternalServerErrorCode int = 500

/*
GetEventInternalServerError Internal service error

swagger:response getEventInternalServerError
*/
type GetEventInternalServerError struct {
}

// NewGetEventInternalServerError creates GetEventInternalServerError with default headers values
func NewGetEventInternalServerError() *GetEventInternalServerError {

	return &GetEventInternalServerError{}
}

// WriteResponse to the client
func (o *GetEventInternalServerError) WriteResponse(rw http.ResponseWriter, producer runtime.Producer) {

	rw.Header().Del(runtime.HeaderContentType) //Remove Content-Type on empty responses

	rw.WriteHeader(500)
}

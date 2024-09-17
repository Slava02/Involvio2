// Code generated by go-swagger; DO NOT EDIT.

package spaces

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"net/http"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime/middleware"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// NewGetSpaceParams creates a new GetSpaceParams object
//
// There are no default values defined in the spec.
func NewGetSpaceParams() GetSpaceParams {

	return GetSpaceParams{}
}

// GetSpaceParams contains all the bound params for the get space operation
// typically these are obtained from a http.Request
//
// swagger:parameters getSpace
type GetSpaceParams struct {

	// HTTP Request Object
	HTTPRequest *http.Request `json:"-"`

	/*space id that is needed
	  Required: true
	  In: path
	*/
	SpaceID int64
}

// BindRequest both binds and validates a request, it assumes that complex things implement a Validatable(strfmt.Registry) error interface
// for simple values it will use straight method calls.
//
// To ensure default values, the struct must have been initialized with NewGetSpaceParams() beforehand.
func (o *GetSpaceParams) BindRequest(r *http.Request, route *middleware.MatchedRoute) error {
	var res []error

	o.HTTPRequest = r

	rSpaceID, rhkSpaceID, _ := route.Params.GetOK("spaceId")
	if err := o.bindSpaceID(rSpaceID, rhkSpaceID, route.Formats); err != nil {
		res = append(res, err)
	}
	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

// bindSpaceID binds and validates parameter SpaceID from path.
func (o *GetSpaceParams) bindSpaceID(rawData []string, hasKey bool, formats strfmt.Registry) error {
	var raw string
	if len(rawData) > 0 {
		raw = rawData[len(rawData)-1]
	}

	// Required: true
	// Parameter is provided by construction from the route

	value, err := swag.ConvertInt64(raw)
	if err != nil {
		return errors.InvalidType("spaceId", "path", "int64", raw)
	}
	o.SpaceID = value

	return nil
}
// Code generated by go-swagger; DO NOT EDIT.

package entity

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"

	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// JoinEventReq join event req
//
// swagger:model JoinEventReq
type JoinEventReq struct {

	// user id
	// Example: 1234
	UserID int64 `json:"user_id,omitempty"`
}

// Validate validates this join event req
func (m *JoinEventReq) Validate(formats strfmt.Registry) error {
	return nil
}

// ContextValidate validates this join event req based on context it is used
func (m *JoinEventReq) ContextValidate(ctx context.Context, formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *JoinEventReq) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *JoinEventReq) UnmarshalBinary(b []byte) error {
	var res JoinEventReq
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
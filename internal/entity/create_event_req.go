// Code generated by go-swagger; DO NOT EDIT.

package entity

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// CreateEventReq create event req
//
// swagger:model CreateEventReq
type CreateEventReq struct {

	// event
	Event *Event `json:"event,omitempty"`

	// space id
	// Example: 1234
	SpaceID int64 `json:"space_id,omitempty"`

	// user id
	// Example: 1234
	UserID int64 `json:"user_id,omitempty"`
}

// Validate validates this create event req
func (m *CreateEventReq) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateEvent(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *CreateEventReq) validateEvent(formats strfmt.Registry) error {
	if swag.IsZero(m.Event) { // not required
		return nil
	}

	if m.Event != nil {
		if err := m.Event.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("event")
			} else if ce, ok := err.(*errors.CompositeError); ok {
				return ce.ValidateName("event")
			}
			return err
		}
	}

	return nil
}

// ContextValidate validate this create event req based on the context it is used
func (m *CreateEventReq) ContextValidate(ctx context.Context, formats strfmt.Registry) error {
	var res []error

	if err := m.contextValidateEvent(ctx, formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *CreateEventReq) contextValidateEvent(ctx context.Context, formats strfmt.Registry) error {

	if m.Event != nil {

		if swag.IsZero(m.Event) { // not required
			return nil
		}

		if err := m.Event.ContextValidate(ctx, formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("event")
			} else if ce, ok := err.(*errors.CompositeError); ok {
				return ce.ValidateName("event")
			}
			return err
		}
	}

	return nil
}

// MarshalBinary interface implementation
func (m *CreateEventReq) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *CreateEventReq) UnmarshalBinary(b []byte) error {
	var res CreateEventReq
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}

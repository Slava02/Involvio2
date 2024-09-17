// Code generated by go-swagger; DO NOT EDIT.

package spaces

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the generate command

import (
	"net/http"

	"github.com/go-openapi/runtime/middleware"
)

// JoinSpaceHandlerFunc turns a function with the right signature into a join space handler
type JoinSpaceHandlerFunc func(JoinSpaceParams) middleware.Responder

// Handle executing the request and returning a response
func (fn JoinSpaceHandlerFunc) Handle(params JoinSpaceParams) middleware.Responder {
	return fn(params)
}

// JoinSpaceHandler interface for that can handle valid join space params
type JoinSpaceHandler interface {
	Handle(JoinSpaceParams) middleware.Responder
}

// NewJoinSpace creates a new http.Handler for the join space operation
func NewJoinSpace(ctx *middleware.Context, handler JoinSpaceHandler) *JoinSpace {
	return &JoinSpace{Context: ctx, Handler: handler}
}

/*
	JoinSpace swagger:route POST /spaces/{spaceId}/join spaces joinSpace

join space
*/
type JoinSpace struct {
	Context *middleware.Context
	Handler JoinSpaceHandler
}

func (o *JoinSpace) ServeHTTP(rw http.ResponseWriter, r *http.Request) {
	route, rCtx, _ := o.Context.RouteInfo(r)
	if rCtx != nil {
		*r = *rCtx
	}
	var Params = NewJoinSpaceParams()
	if err := o.Context.BindValidRequest(r, route, &Params); err != nil { // bind params
		o.Context.Respond(rw, r, route.Produces, route, err)
		return
	}

	res := o.Handler.Handle(Params) // actually handle the request
	o.Context.Respond(rw, r, route.Produces, route, res)

}

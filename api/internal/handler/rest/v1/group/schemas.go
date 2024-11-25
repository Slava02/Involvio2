package group

import "github.com/Slava02/Involvio/api/internal/entity"

// Converters
func ToGroupOutputFromEntity(group *entity.Group) *GroupResponse {
	return &GroupResponse{
		Body: struct{ *entity.Group }{group},
	}
}

type (
	JoinLeaveGroupRequest struct {
		Body struct {
			GroupName string `json:"group_name" example:"123" doc:"Group UserID"`
			UserId    int    `json:"user_id" example:"123" doc:"Group UserID"`
		}
	}

	CreateGroupRequest struct {
		Body struct {
			Name string `json:"name" example:"Very_secret_group_name" doc:"Group Name"`
		}
	}

	UpdateGroupRequest struct {
		ID   int `path:"id" maxLength:"30" example:"1" doc:"group id"`
		Body struct {
			Name        string `json:"name" example:"MAI" doc:"Group Name"`
			Description string `json:"description" example:"university" doc:"Group description"`
		}
	}

	GroupByIdRequest struct {
		ID int `path:"id" json:"id" example:"1" doc:"group id"`
	}

	GroupByNameRequest struct {
		Name string `path:"name" json:"name" example:"MAI" doc:"Group Name"`
	}

	GroupResponse struct {
		Body struct {
			*entity.Group
		}
	}
)

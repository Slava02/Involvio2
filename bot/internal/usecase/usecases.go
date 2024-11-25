package usecase

import (
	"context"
	"fmt"
	client "github.com/Slava02/Involvio/bot/clients"
	"github.com/Slava02/Involvio/bot/internal/models"
	"strings"
)

type UseCases interface {
	AddGroups(ctx context.Context, username string, groups string) (string, error)
	GetGroups(ctx context.Context, username string) (string, error)
}

type UseCase struct {
	apiClient client.ClientWithResponsesInterface
}

func New(apiClient client.ClientWithResponsesInterface) *UseCase {
	return &UseCase{
		apiClient: apiClient,
	}
}

func (uc *UseCase) AddGroups(ctx context.Context, username string, groups string) (string, error) {
	usrResp, err := uc.apiClient.GetUserWithResponse(ctx, username)
	if err != nil {
		return "", fmt.Errorf("couldn't get user: %w", err)
	}

	g := strings.Split(groups, ",")

	newGroups := make([]string, 0)

	for _, group := range g {
		getResp, errGetGroup := uc.apiClient.GetGroupWithResponse(ctx, group)
		_ = getResp
		if errGetGroup != nil {
			return "", fmt.Errorf("%w", errGetGroup)
		}
		if getResp.JSON404 != nil {
			createResp, err := uc.apiClient.CreateGroupWithResponse(ctx, client.CreateGroupJSONRequestBody{
				Name: group,
			})
			_ = createResp

			if err != nil {
				return "", fmt.Errorf("couldn't create group: %w", err)
			}
			newGroups = append(newGroups, group)
		}

		joinResp, err := uc.apiClient.JoinGroupWithResponse(ctx, client.JoinGroupJSONRequestBody{
			GroupName: group,
			UserId:    usrResp.JSON200.Id,
		})
		if err != nil {
			return "", fmt.Errorf("couldn't join group: %w", err)
		}
		_ = joinResp
	}

	if groups[len(groups)-1] == ',' {
		joinResp, err := uc.apiClient.JoinGroupWithResponse(ctx, client.JoinGroupJSONRequestBody{
			GroupName: models.DefaultGroup,
			UserId:    usrResp.JSON200.Id,
		})
		if err != nil {
			return "", fmt.Errorf("couldn't join group: %w", err)
		}
		_ = joinResp
	}

	var groupList string
	if len(newGroups) != 0 {
		if len(newGroups) > 1 {
			groupList = strings.Join(newGroups, ",")
		} else {
			groupList = newGroups[0]
		}
	}

	return groupList, nil
}

func (uc *UseCase) GetGroups(ctx context.Context, username string) (string, error) {
	return "", nil
}

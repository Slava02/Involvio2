package usecase

import (
	"context"
	"fmt"
	"github.com/Slava02/Involvio/internal/entity"
	"time"
)

type IUserRepository interface {
	GetUserData(ctx context.Context, id int) (*entity.User, error)
	GetUserForms(ctx context.Context, userId int) ([]*entity.Form, error)
	InsertUser(ctx context.Context, firstName, lastName, userName, photoURL string, authDate time.Time) (*entity.User, error)
	UpdateUser(ctx context.Context, id int, firstName, lastName, userName, photoURL string) (*entity.User, error)
	DeleteUser(ctx context.Context, userId, spaceId int) error
	GetForm(ctx context.Context, userId, spaceId int) (*entity.Form, error)
	UpdateForm(ctx context.Context, form *entity.Form) (*entity.Form, error)
}

func NewUserUseCase(ur IUserRepository) *UserUseCase {
	return &UserUseCase{userRepo: ur}
}

type UserUseCase struct {
	userRepo IUserRepository
}

func (uc *UserUseCase) GetUser(ctx context.Context, cmd UserByIdCommand) (*entity.User, []*entity.Form, error) {
	userData, err := uc.userRepo.GetUserData(ctx, cmd.ID)
	if err != nil {
		return nil, nil, fmt.Errorf("%w", err)
	}

	userForms, err := uc.userRepo.GetUserForms(ctx, cmd.ID)
	if err != nil {
		return nil, nil, fmt.Errorf("%w", err)
	}

	return userData, userForms, nil
}

func (uc *UserUseCase) DeleteUser(ctx context.Context, cmd FormByIdCommand) error {
	_, err := uc.userRepo.GetUserData(ctx, cmd.UserID)
	if err != nil {
		return fmt.Errorf("%w", err)
	}

	err = uc.userRepo.DeleteUser(ctx, cmd.UserID, cmd.SpaceID)
	if err != nil {
		return fmt.Errorf("%w", err)
	}

	return nil
}

func (uc *UserUseCase) GetForm(ctx context.Context, cmd FormByIdCommand) (*entity.Form, error) {
	form, err := uc.userRepo.GetForm(ctx, cmd.UserID, cmd.SpaceID)
	if err != nil {
		return nil, fmt.Errorf("%w", err)
	}

	return form, nil
}

func (uc *UserUseCase) UpdateForm(ctx context.Context, cmd UpdateFormCommand) (*entity.Form, error) {
	_, err := uc.userRepo.GetUserData(ctx, cmd.UserID)
	if err != nil {
		return nil, fmt.Errorf("%w", err)
	}

	form, err := uc.userRepo.UpdateForm(ctx, cmd.Form)
	if err != nil {
		return nil, fmt.Errorf("%w", err)
	}

	return form, nil
}

func (uc *UserUseCase) CreateUser(ctx context.Context, cmd CreateUserCommand) (*entity.User, error) {
	user, err := uc.userRepo.InsertUser(ctx, cmd.FirstName, cmd.LastName, cmd.UserName, cmd.PhotoURL, cmd.AuthDate)
	if err != nil {
		return nil, fmt.Errorf("%w", err)
	}

	return user, nil
}

func (uc *UserUseCase) UpdateUser(ctx context.Context, cmd UpdateUserCommand) (*entity.User, error) {
	_, err := uc.userRepo.GetUserData(ctx, cmd.ID)
	if err != nil {
		return nil, fmt.Errorf("%w", err)
	}

	user, err := uc.userRepo.UpdateUser(ctx, cmd.ID, cmd.FirstName, cmd.LastName, cmd.UserName, cmd.PhotoURL)
	if err != nil {
		return nil, fmt.Errorf("%w", err)
	}

	return user, nil
}

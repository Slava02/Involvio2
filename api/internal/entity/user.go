package entity

import "time"

// User -.
type User struct {
	ID        int       `doc:"Telegram UserID" json:"id"       example:"1234"`
	FullName  string    `doc:"First name" json:"full_name"       example:"ivan popkins"`
	UserName  string    `doc:"Username" json:"user_name"       example:"s1av4"`
	PhotoURL  string    `doc:"Photo URL" json:"photo_url" example:"https://photo"`
	Birthday  time.Time `doc:"Birthday" json:"birthday"       example:"2020-12-09T16:09:53+00:00"`
	Gender    string    `doc:"User's gender" json:"gender" example:"male"`
	City      string    `doc:"User's city" json:"city" example:"Moscow"`
	Socials   string    `doc:"User's account" json:"socials" exmaple:"https://vk.com"`
	Position  string    `doc:"User's position in organization" json:"position" example:"student"`
	Interests string    `doc:"User's interests" json:"interests" example:"Programming,math"`
	Goal      string    `doc:"User's goal for the meetings" json:"goal" example:"fun"`
	Groups    []Group   `doc:"User's groups" json:"groups"`
}

type Holiday struct {
	Status   bool      `doc:"Whether holiday is active or not" json:"status" example:"true"`
	TillDate time.Time `doc:"When holiday ends RFC 3339" json:"till_date" example:"2020-12-09T16:09:53+00:00"`
	SetDate  time.Time `doc:"When holiday was set RFC 3339" json:"set_date" example:"2020-12-09T16:09:53+00:00"`
}

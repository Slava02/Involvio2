
Enum "gender" {
"f"
"m"
}

Enum "goal" {
"fun"
"profit"
"50_50"
}

Table "group" {
"id" integer [pk]
"name" text [unique, not null]
}

Table "user_group" {
"user_id" integer
"group_id" integer

Indexes {
(user_id, group_id) [pk]
}
}

Table "user" {
"id" integer [unique, not null]
"username" text [unique, not null]
"full_name" text
"birthday" date
"city" varchar
"socials" varchar
"position" varchar
"gender" gender
"photo_url" varchar
"interests" text
"goal" goal
}

Table "holidays_status" {
"id" SERIAL [pk, increment]
"user_id" integer [not null]
"status" bool
"till_date" date [not null]
"set_date" date [not null]
}

Table "event" {
"id" INTEGER [pk, increment]
"date" date
"name" varchar
"description" varchar
}

Table "event_members" {
"id" INTEGER [pk, increment]
"event_id" integer
"user_id" integer
}

Table "reviews" {
"id" SERIAL [pk, increment]
"event_id" integer
"who_id" integer
"about_whom_id" integer
"grade" integer [not null]
}

Table "blocks" {
"who" integer
"whom" integer [not null]
}

Ref:"user"."id" < "user_group"."user_id"

Ref:"group"."id" < "user_group"."group_id"

Ref:"user"."id" < "holidays_status"."user_id"

Ref:"event"."id" < "event_members"."event_id"

Ref:"user"."id" < "event_members"."user_id"

Ref:"event"."id" < "reviews"."event_id"

Ref:"user"."id" < "reviews"."who_id"

Ref:"user"."id" < "reviews"."about_whom_id"

Ref:"user"."id" < "blocks"."who"



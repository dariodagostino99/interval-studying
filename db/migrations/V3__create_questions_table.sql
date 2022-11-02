CREATE TABLE questions (
	id bigserial primary key,
	lesson_id bigint references lessons(id),
	value varchar(255)
);

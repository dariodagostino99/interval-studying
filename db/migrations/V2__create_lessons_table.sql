CREATE TABLE lessons (
	id bigserial primary key,
	topic_id bigint references topics (id)
);

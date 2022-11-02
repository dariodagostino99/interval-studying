CREATE TABLE answers (
        id bigserial primary key,
        question_id bigint references questions(id),
        value varchar(255)
);


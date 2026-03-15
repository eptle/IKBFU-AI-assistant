CREATE TYPE source_enum AS ENUM ('TG', 'VK', 'WEBSITE');


CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE NOT NULL,
    username TEXT,
    first_name TEXT,
    last_name TEXT,

    is_admin BOOLEAN DEFAULT FALSE,
    is_banned BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT NOW(),
    last_activity TIMESTAMP,

    updated_at TIMESTAMP DEFAULT NOW()
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_telegram_id
ON users(telegram_id);


CREATE TABLE posts (
    id BIGSERIAL PRIMARY KEY,

    title TEXT,
    content TEXT NOT NULL,

    link TEXT,
    source source_enum NOT NULL,

    external_id TEXT,

    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_posts_date
ON posts(date);

CREATE INDEX idx_posts_source
ON posts(source);

CREATE UNIQUE INDEX idx_posts_unique_source
ON posts(source, external_id);


CREATE TABLE qa_logs (
    id BIGSERIAL PRIMARY KEY,

    user_id BIGINT REFERENCES users(id),

    question TEXT NOT NULL,
    answer TEXT,

    created_at TIMESTAMP DEFAULT NOW(),

    response_time FLOAT,
    retrieved_docs INT
);

CREATE INDEX idx_qa_logs_user_id
ON qa_logs(user_id);

CREATE INDEX idx_qa_logs_created_at
ON qa_logs(created_at);


CREATE TABLE qa_sources (
    id BIGSERIAL PRIMARY KEY,

    qa_id BIGINT REFERENCES qa_logs(id) ON DELETE CASCADE,
    post_id BIGINT REFERENCES posts(id)
);

CREATE INDEX idx_qa_sources_qa
ON qa_sources(qa_id);

CREATE INDEX idx_qa_sources_post
ON qa_sources(post_id);
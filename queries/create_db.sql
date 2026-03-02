CREATE TYPE source_enum AS ENUM ('TG', 'VK', 'WEBSITE');

CREATE TABLE posts (
    id BIGSERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    link TEXT,
    source source_enum NOT NULL,
    date DATE NOT NULL
);

CREATE INDEX idx_posts_date ON posts(date);
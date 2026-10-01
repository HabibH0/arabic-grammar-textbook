CREATE TABLE IF NOT EXISTS textbook_users (
  id uuid PRIMARY KEY,
  username text UNIQUE NOT NULL,
  password_hash text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS textbook_sessions (
  token_hash text PRIMARY KEY,
  user_id uuid NOT NULL REFERENCES textbook_users(id) ON DELETE CASCADE,
  expires_at timestamptz NOT NULL
);
CREATE INDEX IF NOT EXISTS textbook_sessions_expiry ON textbook_sessions(expires_at);
CREATE TABLE IF NOT EXISTS textbook_progress (
  user_id uuid NOT NULL REFERENCES textbook_users(id) ON DELETE CASCADE,
  module integer NOT NULL CHECK (module BETWEEN 1 AND 999),
  lesson text NOT NULL,
  items jsonb NOT NULL,
  version integer NOT NULL DEFAULT 1,
  updated_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, module, lesson)
);
CREATE TABLE IF NOT EXISTS textbook_rate_limits (
  bucket text PRIMARY KEY,
  count integer NOT NULL,
  expires_at timestamptz NOT NULL
);
-- These tables are private to the backend, never exposed through the Data API.
REVOKE ALL ON textbook_users, textbook_sessions, textbook_progress, textbook_rate_limits FROM PUBLIC;

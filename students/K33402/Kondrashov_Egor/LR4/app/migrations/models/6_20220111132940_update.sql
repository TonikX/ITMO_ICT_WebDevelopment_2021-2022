-- upgrade --
CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL
);
COMMENT ON TABLE "admin" IS 'Модель админки для входа в FastAPI admin';;
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(255) NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_superuser" BOOL NOT NULL  DEFAULT False,
    "is_verified" BOOL NOT NULL  DEFAULT False,
    "first_name" VARCHAR(255),
    "middle_name" VARCHAR(255),
    "last_name" VARCHAR(255),
    "birthdate" DATE
);
CREATE INDEX IF NOT EXISTS "idx_user_email_1b4f1c" ON "user" ("email");
COMMENT ON TABLE "user" IS 'Tortoise user model (fields stored in DB)';;
DROP TABLE IF EXISTS "usermodel";
DROP TABLE IF EXISTS "adminmodel";
-- downgrade --
DROP TABLE IF EXISTS "admin";
DROP TABLE IF EXISTS "user";

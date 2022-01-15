-- upgrade --
CREATE TABLE IF NOT EXISTS "adminmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL
);
-- downgrade --
DROP TABLE IF EXISTS "adminmodel";

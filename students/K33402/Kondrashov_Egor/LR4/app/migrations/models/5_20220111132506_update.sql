-- upgrade --
ALTER TABLE "usermodel" ALTER COLUMN "birthdate" TYPE DATE USING "birthdate"::DATE;
-- downgrade --
ALTER TABLE "usermodel" ALTER COLUMN "birthdate" TYPE TIMESTAMPTZ USING "birthdate"::TIMESTAMPTZ;

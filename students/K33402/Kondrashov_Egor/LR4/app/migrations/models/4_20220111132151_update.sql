-- upgrade --
ALTER TABLE "usermodel" ADD "middle_name" VARCHAR(255);
ALTER TABLE "usermodel" ADD "last_name" VARCHAR(255);
ALTER TABLE "usermodel" ADD "birthdate" TIMESTAMPTZ;
-- downgrade --
ALTER TABLE "usermodel" DROP COLUMN "middle_name";
ALTER TABLE "usermodel" DROP COLUMN "last_name";
ALTER TABLE "usermodel" DROP COLUMN "birthdate";

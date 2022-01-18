-- upgrade --
ALTER TABLE "usermodel" ADD "first_name" VARCHAR(255);
-- downgrade --
ALTER TABLE "usermodel" DROP COLUMN "first_name";

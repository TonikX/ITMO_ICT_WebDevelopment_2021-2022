-- upgrade --
ALTER TABLE "hotel" ADD "address" VARCHAR(1023);
ALTER TABLE "hotel" ADD "img_src" VARCHAR(2047);
ALTER TABLE "hotel" ADD "cost_from" DOUBLE PRECISION;
ALTER TABLE "hotel" ADD "description" TEXT;
ALTER TABLE "hotel" ADD "rating" DOUBLE PRECISION;
-- downgrade --
ALTER TABLE "hotel" DROP COLUMN "address";
ALTER TABLE "hotel" DROP COLUMN "img_src";
ALTER TABLE "hotel" DROP COLUMN "cost_from";
ALTER TABLE "hotel" DROP COLUMN "description";
ALTER TABLE "hotel" DROP COLUMN "rating";

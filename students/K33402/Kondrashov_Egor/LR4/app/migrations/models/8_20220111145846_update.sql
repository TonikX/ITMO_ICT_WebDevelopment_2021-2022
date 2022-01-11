-- upgrade --
CREATE TABLE IF NOT EXISTS "booking" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "starts_at" DATE NOT NULL,
    "ends_at" DATE NOT NULL,
    "number_of_guests" SMALLINT NOT NULL,
    "hotel_id" INT NOT NULL REFERENCES "hotel" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "booking" IS 'Модель бронирования отеля пользователем';
-- downgrade --
DROP TABLE IF EXISTS "booking";

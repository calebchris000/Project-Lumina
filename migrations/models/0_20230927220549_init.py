from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "teacher" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "first_name" VARCHAR(50) NOT NULL,
    "middle_name" VARCHAR(50),
    "last_name" VARCHAR(50) NOT NULL,
    "date_of_birth" TIMESTAMPTZ NOT NULL,
    "email" VARCHAR(30),
    "gender" VARCHAR(6) NOT NULL,
    "date_of_enrollment" DATE,
    "profile_image" VARCHAR(120),
    "roles" VARCHAR(9) NOT NULL  DEFAULT 'guest',
    "subject_taught" VARCHAR(20) NOT NULL,
    "qualifications" VARCHAR(20) NOT NULL,
    "contact" VARCHAR(20) NOT NULL,
    "years_of_experience" DECIMAL(3,1) NOT NULL,
    "supervisor" VARCHAR(20) NOT NULL,
    "attendance_records" VARCHAR(20) NOT NULL,
    "teaching_schedule" VARCHAR(20) NOT NULL
);
COMMENT ON COLUMN "teacher"."gender" IS 'Sex of user';
COMMENT ON COLUMN "teacher"."roles" IS 'SUPERUSER: superuser\nMANAGER: manager\nAUDITOR: auditor\nEMPLOYEE: employee\nGUEST: guest';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

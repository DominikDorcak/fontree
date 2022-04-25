DROP TABLE IF EXISTS "experiment_entry";
DROP SEQUENCE IF EXISTS experiment_entry_id_seq;
CREATE SEQUENCE experiment_entry_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1;

CREATE TABLE "ddorcak"."experiment_entry" (
    "id" bigint DEFAULT nextval('experiment_entry_id_seq') NOT NULL,
    "age" bigint NOT NULL,
    "sex" character NOT NULL,
    "highest_education" bigint NOT NULL,
    "assigned_font" bigint NOT NULL,
    "result_font" bigint NOT NULL,
    "time_in_milis" bigint NOT NULL,
    "question_count" bigint NOT NULL,
    "entry_time" timestamp DEFAULT now() NOT NULL ,
    CONSTRAINT "idx_experiment_entry_primary" PRIMARY KEY ("id")
) WITH (oids = false);


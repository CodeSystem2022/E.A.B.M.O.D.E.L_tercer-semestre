-- Database: test_db

-- DROP DATABASE IF EXISTS test_db;

CREATE DATABASE test_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'es_ES.utf8'
    LC_CTYPE = 'es_ES.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- database: nueva_bd

--drop database if exists nueva_g

CREATE DATABASE nueva_bd
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'EN_us.utf8'
    LC_CTYPE = 'EN_us.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
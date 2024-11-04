#!/bin/bash
set -e

# Variables
DB_NAME="cloud_db"

# Create the database
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE $DB_NAME;
EOSQL

# Create the table and insert data
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$DB_NAME" <<-EOSQL
    CREATE TABLE cloud_vendors (
        vendor_name VARCHAR(100),
        popularity INTEGER
    );

    INSERT INTO cloud_vendors (vendor_name, popularity) VALUES
        ('AWS', 95),
        ('Azure', 90),
        ('Google Cloud', 85),
        ('IBM Cloud', 80),
        ('Oracle Cloud', 75),
        ('Alibaba Cloud', 70),
        ('Salesforce', 65),
        ('SAP Cloud', 60),
        ('Tencent Cloud', 55),
        ('VMware Cloud', 50),
        ('DigitalOcean', 45),
        ('Linode', 40),
        ('Rackspace', 35),
        ('OpenStack', 30),
        ('Heroku', 25),
        ('Cloudflare', 20),
        ('Netlify', 15),
        ('Vultr', 10),
        ('Wasabi', 5),
        ('Backblaze B2', 1);
EOSQL

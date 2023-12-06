psql -c 'drop table award, institution, movie, nomination;' -d postgres -U postgres

python create_tables.py

psql -c "\i sql/seed.sql;" -d postgres -U postgres

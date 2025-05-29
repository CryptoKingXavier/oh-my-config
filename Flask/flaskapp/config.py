from secrets import token_hex

# Neon PostgreSQL Database Connection Parameters
PGPORT = 5432
PGDATABASE = "neondb"
PGPASSWORD = ""
PGUSERNAME = "neondb_owner"
PGHOST = ""

class Config:
  SECRET_KEY = token_hex(16)
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = f"postgresql://{PGUSERNAME}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"

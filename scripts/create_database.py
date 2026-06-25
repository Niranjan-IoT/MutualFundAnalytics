from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/database/mutual_fund.db"
)

connection = engine.connect()

print("Database Created")

connection.close()
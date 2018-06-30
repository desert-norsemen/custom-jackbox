import psycopg2
import config

connectionString = (f"dbname={config.postgres['db']} user={config.postgres['user']} host={config.postgres['host']} password={config.postgres['password']}")

conn = psycopg2.connect(connectionString)

db = conn.cursor()

db.execute("drop table if exists prompts;")
db.execute("create table prompts (prompt_id serial primary key, prompt_text text not null);")
db.execute("insert into prompts (prompt_text) values ('Gold team rules!');")

db.execute("select * from prompts;")
response = db.fetchone()

conn.commit()

db.close()
conn.close()

print(response)
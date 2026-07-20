from sqlalchemy.orm import Session
from shared.config.database import engine


def upsert_records(table: str, records: list) -> int:
    """Upsert records into a table. Returns count of synced records."""
    total_synced = 0
    conn = engine.raw_connection()
    try:
        cursor = conn.cursor()
        for row in records:
            row_data = {k: v for k, v in row.items() if k != "is_synced"}
            if not row_data:
                continue

            pk = list(row_data.keys())[0]
            pk_value = row_data[pk]

            check = cursor.execute(
                f"SELECT COUNT(*) FROM {table} WHERE {pk} = %(val)s",
                {"val": pk_value},
            )
            exists = cursor.fetchone()[0] > 0

            if exists:
                set_clause = ", ".join([f"{k} = %({k})s" for k in row_data.keys()])
                cursor.execute(
                    f"UPDATE {table} SET {set_clause} WHERE {pk} = %(pk_val)s",
                    {**row_data, "pk_val": pk_value},
                )
            else:
                cols = ", ".join(row_data.keys())
                vals = ", ".join([f"%({k})s" for k in row_data.keys()])
                cursor.execute(
                    f"INSERT INTO {table} ({cols}) VALUES ({vals})",
                    row_data,
                )
            conn.commit()
            total_synced += 1
    finally:
        cursor.close()
        conn.close()
    return total_synced


def pull_records(table_list: list, last_sync: str | None = None) -> dict:
    """Pull records from tables. Returns dict of table_name -> rows."""
    result = {}
    conn = engine.raw_connection()
    try:
        cursor = conn.cursor()
        for table in table_list:
            if last_sync:
                cursor.execute(
                    f"SELECT * FROM {table} WHERE updated_at >= %(last_sync)s OR created_at >= %(last_sync)s",
                    {"last_sync": last_sync},
                )
            else:
                cursor.execute(f"SELECT * FROM {table}")

            columns = [desc[0] for desc in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
            for row in rows:
                for k, v in row.items():
                    if hasattr(v, "isoformat"):
                        row[k] = v.isoformat()
            result[table] = rows
    finally:
        cursor.close()
        conn.close()
    return result

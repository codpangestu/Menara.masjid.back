from typing import Optional
from services.transaction_service.queries.sync_queries import upsert_records, pull_records


class SyncService:
    def push(self, data: dict) -> dict:
        """Sync push from mobile app."""
        total_synced = 0
        for table, records in data.items():
            if not records:
                continue
            total_synced += upsert_records(table, records)
        return {
            "status_code": "200",
            "message": "Sync Push Success",
            "total_synced": total_synced,
        }

    def pull(self, tables: Optional[str] = None, last_sync: Optional[str] = None) -> dict:
        """Sync pull for mobile app."""
        default_tables = ["masjid", "kas", "bukukas_penerimaan", "bukukas_pengeluaran"]
        if tables:
            table_list = [t.strip() for t in tables.split(",")]
        else:
            table_list = default_tables

        result = pull_records(table_list, last_sync)
        return {
            "status_code": "200",
            "data": result,
        }

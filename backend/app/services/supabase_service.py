import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class SupabaseService:
    def __init__(self):
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        if not url or not key:
            print("Warning: Supabase credentials missing from .env")
        else:
            self.client: Client = create_client(url, key)

    async def log_signal(self, signal_data: dict):
        """Log a behavioral signal to the cloud."""
        return self.client.table("iblm_signals").insert(signal_data).execute()

    async def get_kernel(self, user_id: str):
        """Retrieve the child's learning kernel."""
        res = self.client.table("iblm_kernels").select("*").eq("user_id", user_id).execute()
        return res.data[0] if res.data else None

    async def upsert_kernel(self, kernel_data: dict):
        """Save or update the child's learning kernel."""
        return self.client.table("iblm_kernels").upsert(kernel_data).execute()

db_service = SupabaseService()

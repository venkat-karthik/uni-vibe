"""WSGI entry point for Vercel deployment"""
import os
import sys

# Set environment variable for Vercel
os.environ['VERCEL'] = '1'

from app import app, init_db

# Initialize database on startup
try:
    init_db()
    print("✅ Database initialized")
except Exception as e:
    print(f"⚠️ Database initialization warning: {e}")

if __name__ == "__main__":
    app.run()

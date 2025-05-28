#!/usr/bin/env python3
"""
Test script to verify frontend functionality.
"""

import uvicorn
import webbrowser
import time
import threading
from pathlib import Path

def start_server():
    """Start the FastAPI server."""
    try:
        uvicorn.run(
            "lawfirm_rag.api.fastapi_app:app",
            host="127.0.0.1",
            port=8000,
            reload=False,
            log_level="info"
        )
    except Exception as e:
        print(f"Error starting server: {e}")

def test_frontend():
    """Test the frontend by opening it in browser."""
    print("🚀 Starting LawFirm-RAG Frontend Test...")
    
    # Check if frontend files exist
    frontend_path = Path("frontend/dist")
    if not frontend_path.exists():
        print("❌ Frontend directory not found!")
        return
    
    index_file = frontend_path / "index.html"
    css_file = frontend_path / "assets" / "styles.css"
    js_file = frontend_path / "assets" / "app.js"
    
    print(f"✅ Frontend files check:")
    print(f"   - index.html: {'✅' if index_file.exists() else '❌'}")
    print(f"   - styles.css: {'✅' if css_file.exists() else '❌'}")
    print(f"   - app.js: {'✅' if js_file.exists() else '❌'}")
    
    if not all([index_file.exists(), css_file.exists(), js_file.exists()]):
        print("❌ Missing frontend files!")
        return
    
    print("\n🌐 Starting FastAPI server...")
    
    # Start server in background thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    
    # Test URLs
    test_urls = [
        "http://127.0.0.1:8000/health",
        "http://127.0.0.1:8000/app",
        "http://127.0.0.1:8000/assets/styles.css",
        "http://127.0.0.1:8000/assets/app.js"
    ]
    
    print("\n🧪 Testing endpoints:")
    for url in test_urls:
        print(f"   - {url}")
    
    print(f"\n🎉 Frontend should be available at: http://127.0.0.1:8000/app")
    print("📝 Note: You'll need an API key to use the full functionality")
    print("🛑 Press Ctrl+C to stop the server")
    
    # Open browser
    try:
        webbrowser.open("http://127.0.0.1:8000/app")
    except Exception as e:
        print(f"Could not open browser: {e}")
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")

if __name__ == "__main__":
    test_frontend() 
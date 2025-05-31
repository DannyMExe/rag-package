#!/usr/bin/env python3
"""
Debug script to check RAG environment and sys.path issues.
"""

import sys
import os
from pathlib import Path

def main():
    print("=== RAG Environment Debug ===")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Virtual env: {os.environ.get('VIRTUAL_ENV', 'None')}")
    print()
    
    print("=== Current sys.path ===")
    for i, path in enumerate(sys.path):
        print(f"{i}: {path}")
    print()
    
    # Try to find RAG environment
    try:
        from lawfirm_rag.cli.env_manager import find_rag_environment, is_in_rag_env
        
        rag_env = find_rag_environment()
        print(f"RAG environment found: {rag_env}")
        print(f"Is in RAG env: {is_in_rag_env()}")
        
        if rag_env:
            # Check if site-packages exists
            if sys.platform == "win32":
                site_packages = rag_env / "Lib" / "site-packages"
            else:
                site_packages = rag_env / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
            
            print(f"Site packages path: {site_packages}")
            print(f"Site packages exists: {site_packages.exists()}")
            
            if site_packages.exists():
                # Check what's in site-packages
                st_path = site_packages / "sentence_transformers"
                chromadb_path = site_packages / "chromadb"
                torch_path = site_packages / "torch"
                
                print(f"sentence-transformers installed: {st_path.exists()}")
                print(f"chromadb installed: {chromadb_path.exists()}")
                print(f"torch installed: {torch_path.exists()}")
                
                # Try manual sys.path modification
                if str(site_packages) not in sys.path:
                    print(f"\n⚠️  Site packages not in sys.path! Adding manually...")
                    sys.path.insert(0, str(site_packages))
                    print("Added to sys.path")
                else:
                    print("✅ Site packages already in sys.path")
        
    except ImportError as e:
        print(f"❌ Can't import RAG modules: {e}")
    
    print("\n=== Testing imports ===")
    
    # Test imports
    try:
        import sentence_transformers
        print("✅ sentence-transformers imported successfully")
        print(f"   Version: {sentence_transformers.__version__}")
        print(f"   Location: {sentence_transformers.__file__}")
    except ImportError as e:
        print(f"❌ sentence-transformers import failed: {e}")
    
    try:
        import torch
        print("✅ torch imported successfully")
        print(f"   Version: {torch.__version__}")
        print(f"   Location: {torch.__file__}")
    except ImportError as e:
        print(f"❌ torch import failed: {e}")
    
    try:
        import chromadb
        print("✅ chromadb imported successfully")
        print(f"   Version: {chromadb.__version__}")
        print(f"   Location: {chromadb.__file__}")
    except ImportError as e:
        print(f"❌ chromadb import failed: {e}")

if __name__ == "__main__":
    main() 
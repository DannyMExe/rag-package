#!/usr/bin/env python3
"""
Improved dependency check with progress indicators.
Shows what the CLI should be doing.
"""

import sys
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def check_dependencies_with_progress():
    """Check dependencies with user-friendly progress indicators."""
    
    deps_to_check = [
        ("torch", "PyTorch (Deep Learning)"),
        ("sentence_transformers", "Sentence Transformers (Embeddings)"),
        ("chromadb", "ChromaDB (Vector Database)")
    ]
    
    missing_deps = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=False
    ) as progress:
        
        for dep_name, friendly_name in deps_to_check:
            task = progress.add_task(f"Checking {friendly_name}...", total=1)
            
            try:
                start_time = time.time()
                exec(f"import {dep_name}")
                duration = time.time() - start_time
                
                progress.update(task, description=f"✅ {friendly_name} loaded ({duration:.1f}s)")
                progress.advance(task)
                
            except ImportError:
                progress.update(task, description=f"❌ {friendly_name} not found")
                progress.advance(task)
                missing_deps.append(dep_name)
    
    if missing_deps:
        console.print(f"\n[red]❌ Missing dependencies: {', '.join(missing_deps)}[/red]")
        return False
    else:
        console.print("\n[green]🎉 All dependencies loaded successfully![/green]")
        return True

if __name__ == "__main__":
    print("Testing improved dependency checking...")
    check_dependencies_with_progress() 
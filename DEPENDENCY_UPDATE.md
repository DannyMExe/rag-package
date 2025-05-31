# Dependency Update - Working Versions

## Summary
Updated the lawfirm-rag package to use **tested working versions** of dependencies based on real-world testing.

## Key Changes

### 1. Updated Core Dependencies
- **PyTorch**: `2.1.0` → `2.1.0+cpu` (with CPU-specific index URL)
- **Sentence Transformers**: `2.2.2` → `4.1.0` (latest stable version)
- **Removed extra torch dependencies**: `torchvision`, `torchaudio` (not needed)

### 2. PyTorch Installation Method
Updated to use the CPU-optimized PyTorch installation:
```bash
pip install torch==2.1.0+cpu --index-url https://download.pytorch.org/whl/cpu
```

### 3. Environment Variables for Stability
Added automatic configuration of PyTorch stability variables:
```bash
export PYTORCH_DISABLE_PLATFORM_CHECK=1  # Prevents platform compatibility errors
export OMP_NUM_THREADS=1                  # Optimizes CPU performance
```

## Technical Implementation

### Files Updated
1. **requirements.txt** - Updated with working versions and installation notes
2. **pyproject.toml** - Updated dependencies with platform-specific torch installation
3. **lawfirm_rag/cli/env_manager.py** - Enhanced with:
   - Separate PyTorch installation logic with CPU index URL
   - Automatic environment variable setup
   - Helper scripts for environment configuration
4. **README.md** - Updated system requirements and environment setup documentation

### New Features in env_manager.py
- **PYTORCH_REQUIREMENTS**: Separate handling for PyTorch with CPU index URL
- **PYTORCH_ENV_VARS**: Automatic configuration of stability variables
- **_setup_pytorch_env_vars()**: Creates helper scripts for environment setup
- **Enhanced activation**: Applies environment variables when activating

### Environment Scripts Created
The setup now creates helper scripts in the virtual environment:
- **Windows**: `pytorch_env.bat`, `pytorch_env.ps1`
- **Unix**: `pytorch_env.sh` (executable)
- **Cross-platform**: `check_pytorch_env.py` for verification

## User Experience

### Before
```bash
pip install rag-package
rag setup  # Sometimes failed with PyTorch compatibility issues
```

### After
```bash
pip install rag-package
rag setup  # Uses tested working versions with automatic stability config
```

### Benefits
- ✅ **Higher Success Rate**: Uses proven dependency versions
- ✅ **Better Stability**: Automatic PyTorch environment configuration
- ✅ **Latest Features**: Upgraded to sentence-transformers 4.1.0
- ✅ **Better Performance**: CPU-optimized PyTorch installation
- ✅ **Automatic Recovery**: Environment variables prevent common hanging issues

## Compatibility
- **Python**: Requires 3.11+ (unchanged)
- **PyTorch**: CPU-optimized for maximum compatibility across systems
- **Platform Support**: Windows, macOS, Linux with automatic environment configuration
- **ARM64**: Separate torch installation for Apple Silicon support

## Testing Notes
These versions were validated through real-world testing and represent the most stable combination for the package's AI/ML functionality. 
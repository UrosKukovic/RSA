@echo off
setlocal enabledelayedexpansion

for /f "tokens=* delims=" %%a in (encrypted.txt) do (
    set "line=%%a"
    set "line=!line:[=!"
    set "line=!line:]=!"
    set "line=!line:,=!"
    if "!line:~-1!"==" " set "line=!line:~0,-1!" 
    
    echo !line!>>encrypted_new.txt
)

move /y encrypted_new.txt encrypted.txt
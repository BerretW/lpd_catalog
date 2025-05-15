@echo off
setlocal

REM Vytvoření adresářové struktury
mkdir backend
cd backend
mkdir models schemas crud

REM Hlavní soubory
type nul > main.py
type nul > config.py
type nul > database.py
type nul > init_db.py

REM Soubory v podsložkách
for %%F in ("__init__.py" "base.py" "organization.py" "object.py" "device.py" "power_source.py" "battery.py" "battery_type.py" "device_type.py" "power_source_type.py") do (
    type nul > models\%%F
    type nul > schemas\%%F
    type nul > crud\%%F
)

REM Přidání __init__.py souborů pro složky
type nul > models\__init__.py
type nul > schemas\__init__.py
type nul > crud\__init__.py

echo Projektová struktura byla vytvořena.
pause

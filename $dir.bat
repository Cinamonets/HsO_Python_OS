@echo off
title Disk Source Editor

:disk scanner
dir
echo Disk.
set /p disk=Option: 

if %settings_choice%==1 goto customization
if %settings_choice%==2 goto change_password
if %settings_choice%==3 goto change_username
if %settings_choice%==4 goto main

@echo off

echo ==============================
echo Python Environment Setup
echo ==============================

echo.
echo Upgrading pip...
python -m pip install --upgrade pip --user

echo.
echo Clearing pip cache...
python -m pip cache purge

echo.
echo Installing packages...
python -m pip install --user opencv-python
python -m pip install --user numpy
python -m pip install --user pillow
python -m pip install --user pyaudio

echo.
echo Installing face_recognition dependencies...
python -m pip install --user cmake
python -m pip install --user dlib
python -m pip install --user face_recognition

echo.
echo ==============================
echo Installation Complete
echo ==============================

pause

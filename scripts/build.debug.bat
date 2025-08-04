@echo off
python -m nuitka --standalone --mingw64 ^
    --plugin-enable=pyside6 ^
    --output-dir=dist ^
    --windows-icon-from-ico=yolo_ui\resources\icon.ico ^
    --python-flag=no_docstrings,no_asserts ^
    --assume-yes-for-downloads ^
    --windows-console-mode=force ^
    main.py

:EOF

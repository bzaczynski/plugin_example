#!/bin/bash

# Generate alert.zip
pushd alert
zip -r ../alert.zip .
popd

# Generate sound.zip
pushd sound
#python -m pip install requests playsound --target ./playsound
python -m pip install requests --target ./requests
python -m pip install python-vlc --target .
#python -m pip install playsound --target ./playsound
zip -r ../sound.zip .
popd

# Move zip files to the plugins/ folder
mv *.zip ../test/plugins/

# Run the main script
pushd ../test/
PYTHONPATH=plugins/sound.zip python main.py
popd

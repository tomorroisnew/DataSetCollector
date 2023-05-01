# DataSetCollector

How to use?
1. Download Python 3.10.11 in https://www.python.org/downloads/release/python-31011/
2. Run the installer, press "Add Python.exe to path"
3. Press "Install Now"
4. In the top-right corner of this repository, click the green button "<> Code"
5. Press "Download ZIP"
6. Unzip the ZIP file anywhere but remember the location
7. Open the folder of the DataSetCollector
8. Type CMD in the folder
9. (Optional) If CMD not opened in folder, change directory to it by right-clicking the folder, then "Properties", there you will see the Location (example: C:\Users\Jocher\Desktop), copy the location then type in CMD `cd "PASTE THE LOCATION HERE"` then another `cd DataSetCollector-main`
10. Type and Enter `py -3 -m pip install -r requirements.txt`
11. Open DataSetCollector.py in any file editor and when you scroll down, you will see the following lines of code:
```py
    if(results.multi_hand_landmarks):
        for hand_landmarks in results.multi_hand_landmarks:
            if(keyboard.is_pressed("A") and not recording):
                recording = True
                print("recording Started")
                gesture = "A"

            if(keyboard.is_pressed("J") and not recording):
                recording = True
                print("recording Started")
                gesture = "J"

            if(keyboard.is_pressed("B") and not recording):
                recording = True
                print("recording Started")
                gesture = "B"

            if(keyboard.is_pressed("D") and not recording):
                recording = True
                print("recording Started")
                gesture = "D"

            if(keyboard.is_pressed("Z") and not recording):
                recording = True
                print("recording Started")
                gesture = "Z"

            if(keyboard.is_pressed("Y") and not recording):
                recording = True
                print("recording Started")
                gesture = "YES"

            if(keyboard.is_pressed("2") and not recording):
                recording = True
                print("recording Started")
                gesture = "2Joints"
```
12. To record a different word, replace the `gesture = "WORD"` to any other word, for example `gesture = "Hello"`, `gesture = "Thank_you"`
13. To initiate recording, press the key that is in `keyboard.is_pressed("A")`, you can change this to any other key
14. Run the DataSetCollector.py by typing in the same CMD `py -3 DataSetCollector.py`
15. The DataSetCollector collects the position of the hand in the last 30 frames and will be collected within one second.
16. Keep recording until you have recorded 50 to 100 data.
17. Update the provided spreadsheet and upload the data.
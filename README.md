# DataSetCollector

Pano Gamitin 
1. Download muna python dito https://www.python.org/downloads/
2. Run nyo yung installer, sa installer, may option na Add Python.exe to path. check nyo yon, tapos Install Now
3. Download nyo tong repository na to. Sa upper right, may makikita kayo <> Code, pindutin nyo yon tapos download as zip
4. Unzip nyo kahit saan, tandaan nyo yung file location kung saan nyo inextract
5. Bukas kayo ng cmd sa kung saan nyo inextract, kunwari ako, inextract ko sa C:\Users\Magic Media\Desktop\DataSetCollector-main, change directory muna sa folder na yon
`cd C:\Users\Magic Media\Desktop\DataSetCollector-main`, tapos run nyo `py -3 -m pip install -r requirements.txt`
6. Buksan nyo yung DataSetCollector.py sa kahit anong file editor, sa baba, makikita nyo yubg mga lines na 
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
Kung gusto nyo magrecord ng ibang word, kunwari yung word na tite, Sa kahit anong line don, palitan nyo lang yung `gesture =`, kunwari yung `gesture = "A"`, gagawin mong `gesture = "tite"`, tapos, pagmagrerecord, yung pipindutin mo, yung nasa `keyboard.is_pressed("A")`
7. Run nyo na yung DataSetCollector.py gamit `py -3 DataSetCollector.py`
8. Tapos pindutin nyo na yung keyword. 
9. Yung pagrerecord, ay 30 fps, nagcocollect ng 30 frames, ibig sabihin, may isang segundo ka para gawin yung sign language habang nagrerecord. 
10. Ulitin mo yung pagrerecord hanggang maka kuha ka ng 30 na data. Pag gusto mo magrecord ng ibang words, palitamn mo lang yung nasa gesture

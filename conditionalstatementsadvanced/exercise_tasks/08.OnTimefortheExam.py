hour_exam=int(input())
minutes_exam=int(input())
hour_arrival=int(input())
minutes_arrival=int(input())

mins_exam = hour_exam*60 +minutes_exam
mins_arrival = hour_arrival*60 + minutes_arrival

razlika = mins_exam-mins_arrival

if 0<=(razlika)<=30:
    print("On time")
    if mins_exam==mins_arrival:
        exit()
    else:
        print(f"{mins_exam-mins_arrival} minutes before the start")
elif razlika>30:
    print("Early")
    if razlika<60:
        print(f"{razlika} minutes before the start")
    else:
        hours = razlika//60
        minutes = razlika%60
        minutes = "0"+str(minutes) if minutes<10 else minutes
        print(f"{hours}:{minutes} hours before the start")
elif razlika<0:
    print("Late")
    razlika=abs(razlika)
    if razlika<60:
        print(f"{razlika} minutes after the start")
    else:
        hours = razlika//60
        minutes = razlika%60
        minutes = "0"+str(minutes) if minutes<10 else minutes
        print(f"{hours}:{minutes} hours after the start")

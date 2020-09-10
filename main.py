#Author : Nicole Giron nqg5259@psu.edu

def letterGrade(score):
  if score >= 93.0:
    return "A"
  elif score >= 90.0 and score < 93.0:
    return "A-"
  elif score >= 87.0 and score < 90.0:
    return "B+"
  elif score >= 83.0 and score < 87.0:
    return "B"
  elif score >= 80.0 and score < 83.0:
    return "B-"
  elif score >= 77.0 and score < 80.0:
    return "C+"
  elif score >= 70.0 and score < 77.0:
    return "C"
  elif score >= 60.0 and score < 70.0:
    return "D"
  else:
    return "F"


grade = float(input("Enter your CMPSC 131 grade: "))
print("Grade point for course 1 is: " + str(letterGrade(grade)))
def isfloat(n):
  """ 
  If string can be converted to floating number 
  returns that number, otherwise returns false
  """
  try:
    n=float(n)
    return n;
  except ValueError:
     return False;

def inputfloat(hint):
  """ 
  Prints hint and asks to enter number.
  Repeats until decimal number is entered.
  """
  ret = False
  while ret is False:
    ret = isfloat(input(hint))
    if ret is False:
      print("Please enter number")
  return ret 

class BMIcalculator:
  def getdata(this):
    """
    Get weight in kgs and height in cms.
    Height is entered in cetimetres and stored in metres
    """

    this.w = inputfloat("Please enter your weight in kilograms:")
    this.h = inputfloat("Please enter your height in centimetres:")/100

  def calculate(this):
    """
    Calculate and return bmi
    """

    return round(this.w/(this.h*this.h),2)


def main():
  print("\n","="*42,"\n")
  print("Hello, let's calculate your BMI.");
  
  calc = BMIcalculator()
  print()
  calc.getdata()
  bmi=calc.calculate()
  print(f"Your BMI is {bmi}")
  print("\n","="*42,"\n")

if __name__ == "__main__":
    main()
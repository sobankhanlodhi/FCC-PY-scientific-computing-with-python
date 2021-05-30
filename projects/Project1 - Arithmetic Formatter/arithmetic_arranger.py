def arithmetic_arranger(problems, ansflag = False):

  if len(problems)>5:
    return "Error: Too many problems."
  else:
    
    topLine = ''
    secondLine = ''
    dashLine = ''
    answerLine = ''

    arranged_problems = []
    for i, problem in enumerate(problems):
      sepStr = problem.split()
      num1 = sepStr[0]
      num2 = sepStr[2]
      operand = sepStr[1]

      #The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
      if operand not in ["+", "-"]:
        return "Error: Operator must be '+' or '-'." 
      else:
        #Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
        for digit in num1:
          if digit.isnumeric():
            continue            
          else: 
            return "Error:  Numbers must only contain digits." 

        for digit in num2:
          if digit.isnumeric():
            continue
          else:             
            return "Error: Numbers must only contain digits." 

        #Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
        if len(num1)>4 or len(num2)>4:
          return "Error: Numbers cannot be more than four digits."
        else: 

            if operand == '-':
              answer = int(num1) - int(num2)
            else: 
              answer = int(num1) + int(num2)
            
            width = max(len(num1),len(num2)) +2
            
            #Numbers should be right-aligned.
            topLine += str(num1.rjust(width))
            
            #Numbers should be right-aligned.
            secondLine +=  str(operand + num2.rjust(width-1)) 
            
            #There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
            dashLine += str("-" * width)

            #Numbers should be right-aligned.
            answerLine += str(answer).rjust(width)

            #There should be four spaces between each problem.
            if i < len(problems)-1:
              topLine += "    "
              secondLine += "    "
              dashLine += "    "
              answerLine += "    "
            
            #The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.
            if ansflag == True: 
              arranged_problems = (topLine + "\n" + secondLine + "\n" + dashLine + "\n" + answerLine)
            else: 
              arranged_problems = (topLine + "\n" + secondLine + "\n" + dashLine)


  return arranged_problems
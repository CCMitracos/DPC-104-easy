# DPC 104 [E]
# Powerplant Simulation


play = True
while (play == True):

  k = int(raw_input("\nNumber of days comissioned >> "))
  
  r = 2*(k/3)+(k%3)-(k/100-k/300) - (2*((k/14)/3) + ((k/14)%3)) + k/700
  
  print "\nNumber of days to run:", r
  
  if (raw_input("\nq to quit")=="q"):
    play = False

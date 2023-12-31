### General
- Months represent status at the beginning of the month
- Are interest rates (risk-free and S&P) normally distributed? or Uniform? or What?
  - Maybe normal with an unusual standard deviation?
  - Make chart showing this and explain to user
  - Should I use S&P interest rates in actuality? Or just say, "They're normal, so we're using normal"?
- Need to maybe allow non-variable fields upon request (i.e. don't vary interest, or don't vary savings added per month)
- Right now, there are yearly (base) interest and monthly (base) interest list being generated. But these are static variables,
so really don't need lists. Only really needed for outputting to csv
- Have a thing that calculates total salary for each month (so like money invested + spent + saved) and use as a check
- Re-work counts and everything for pre-retirement count, post-retirement count and a total count
  - And months
- Are you working?
- Are you still contributing to retirement?
- Are you withdrawing SS?
- What are your monthly bills?
- What are your extra monthly bills?
- Does your market interest change post-retirement?
- How to deal with health care
- I think I need to reevaluate the randomness here. E.g. it's not very likely that you will double your savings. But more likely you will go down to 0. So skew it lower more than higher.
- Write unit tests
- Get isort, etc hooked into CI
  - Do I need GH actions for this? Does it cost?
- It would be good to have it calculate back from 110 (or whatever) and show you how much you would need at each age of retirement
  - This would be part of a suite of results/outputs from the calculations
  - Helpful to know how much more you'd need at 55 versus 60 versus 65, etc.
- Add logging

##Inputs
- (.json)
  - Use pydantic to validate
  - Make sure all inputs are in todays dollars
    - Adjust everything else accordingly
      - Looking at you lower-limit savings amount
  - Year over year changes to retirement and savings should be the same type (percent versus total dollars)
    - Maybe eventually have this be an option for both?
- Website
  - Figure out how non-base payments can be an empty list
  - Make a note saying everything should be in today's dollars
  - Pass in everything as string and validate from there?
  - Better names for the input fields
  - Make payments be able to be added dynamically, multiple times
  - Have modals pop up on mouse-over with explanations
  - Maybe have sections for each type of input (savings, retirement, base bills/savings, non-base payments, etc.)
    - You could create multiple and then mix and match or something like that?

## Savings
- Do I need to make a new variable for savings interest? Usually lower and less volatile - continuous flow
- Idea: Have interest rate change every quarter and choose a direction and magnitude between 0.05% and 0.15%?
  - Floor at 0.1%, cap at 5.5%?
  - This is essentially adjusted via uniform distribution. Should I change this? Look at historical data and see what's what?
    - Yeah, doesn't look like a ton of variance. But maybe that's OK?
- Adjust amount saved per month
  - Do this via annual pay raises (actually, should ultimately make this user-generated frequency)
    - This also adjusts for inflation assuming your pay is inflation-adjusted
  - Can do a flat savings increase or a percentage
- Add bonuses eventually
- Make it so that savings can't go negative is retirement is positive
- Should the frequency that the rf rate changes be something the user can input? Seems like not

## Social Security
- SS withdraw amount could be assumed, or calculated
  - Should also have an override for if SS is assumed at all upon retirement
- Can you withdraw SS beginning at any age/month combo?

## Payments
- Need to make car payment more dynamic (start, stop, multiple occurrences)
- Make new cars have some chaos variable where it gets destroyed and you need a new one or something
- Add in optional TVM calc for payments per month
- Right now the person has to enter in their information one at a time (like for cars). Should there be a thing to just says, 
  "buy new car every X years, and just adjust according to inflation?"
- Need to add an employer contribution bit
  - I suppose this could be baked into the monthly, but if you're like me with annual contributions, then you'd need something extra
- I think this could maybe account for negative payments (i.e. savings) as well?
  - If you expect to have a reverse mortgage, or an annuity or something like that, this would be able to be input here as negative amounts?
  - Maybe should be its own thing?
- Since this is getting stored as a dictionary, can't have duplicate names. Need to fix.
  
## Retirement
- Change it so that retirement increase only changes at the start of a calendar year
- What money are you pulling from where?
- Reverse mortgage?
- This kind of assumes a Roth style account where taxes aren't a thing. Probably should add logic to deal with that
- Maybe use the costs calculated and TVM that back to figure out the present value of all of that to give a retirement value
- Make it so that retirement can't go negative is savings is positive

## Outputs
- Need to format dollars using some sort of function
  - Negatives, percentages
  
#Front End
- Make it easier to update forms without redirecting to a new webpage
  - Formsets? Inline formsets?
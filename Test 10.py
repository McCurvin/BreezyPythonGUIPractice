from breezypythongui import EasyFrame
class TextAreaDemo(EasyFrame):
    def __init__(self):
        """An investment calculator demonstrates the use of a
         multi-line text area."""
        EasyFrame.__init__(self, "Investment Calculator")
        self.addLabel(text = "Initial amount", row = 0, column = 0)
        self.addLabel(text = "Number of years", row = 1, column = 0)
        self.addLabel(text = "Interest rate in %", row = 2, column = 0)
        self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
        self.period = self.addIntegerField(value = 0, row = 1, column = 1)
        self.rate = self.addIntegerField(value = 0, row = 2, column = 1)
        self.outputArea = self.addTextArea("", row = 4, column = 0,columnspan = 2, width = 50,height = 15)
        self.compute = self.addButton(text = "Compute", row = 3,column =
        0,columnspan = 2,command = self.compute)

# Event handling method.
    def compute(self):
        # Obtain and validate the inputs
        startBalance = self.amount.getNumber()
        rate = self.rate.getNumber() / 100
        years = self.period.getNumber()
        if startBalance == 0 or rate == 0 or years == 0:
            return
        # Set the header for the table
        result = "%4s%18s%10s%16s\n" % ("Year", "Starting balance","Interest","Ending balance")

        # Compute and append the results for each year
        totalInterest = 0.0
        for year in range(1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d%18.2f%10.2f%16.2f\n" % \
                      (year, startBalance, interest, endBalance)
            startBalance = endBalance
            totalInterest += interest


        # Append the totals for the period
        result += "Ending balance: $%0.2f\n" % endBalance
        result += "Total interest earned: $%0.2f\n" % totalInterest


        # Output the result while preserving read-only status
        self.outputArea["state"] = "normal"
        self.outputArea.setText(result)
        self.outputArea["state"] = "disabled"
TextAreaDemo().mainloop()
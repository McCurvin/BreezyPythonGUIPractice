from breezypythongui import EasyFrame


class SimplePayroll(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "Wage Calculator")
        infoPanel = self.addPanel(row=0, column=0, background="pink")

        infoPanel.addLabel(text="Rate Per Hour: ", row=0, column=0, background="pink")
        self.txtRPH = infoPanel.addTextField(text="0.0", row=0, column=1, width=10)

        infoPanel.addLabel(text="Hours worked: ", row=1, column=0, background="pink")
        self.txtHW = infoPanel.addTextField(text="0.0", row=1, column=1, width=10)

        infoPanel.addLabel(text="Gross Pay: ", row=2, column=0, background="pink")
        self.txtGrossPay = infoPanel.addTextField(text="0.0", row=2, column=1, width=10, state="readonly")

        infoPanel.addLabel(text="Deduction: ", row=3, column=0, background="pink")
        self.txtDeduction = infoPanel.addTextField(text="0.0", row=3, column=1, width=10)

        infoPanel.addLabel(text="Net Pay: ", row=4, column=0, background="pink")
        self.txtNetPay = infoPanel.addTextField(text="0.0", row=4, column=1, width=10, state="readonly")

        # Button
        self.btnProcess = infoPanel.addButton(text="Calculate", row=5, column=0, columnspan=2, command=self.process)
        self.btnProcess.configure(background="white", foreground="gray", activeforeground="yellow")

        # Display
        self.display = "RPH\tHW\tGross\t\tDeduction\t\tNet\n"
        self.txtOutput = self.addTextArea(text=self.display, row=6, column=0, width=60, height=20)

        # Event handling method.

    def process(self):
        # Calculating Gross Pay
        ratePerHour = float(self.txtRPH.getText())
        hoursWorked = float(self.txtHW.getText())
        grossPay = ratePerHour * hoursWorked
        self.txtGrossPay.setText(f"{grossPay:.2f}")

        # Calculating Net Pay
        deduction = float(self.txtDeduction.getText())
        netPay = grossPay - deduction
        self.txtNetPay.setText(f"{netPay:.2f}")

        # Results
        self.txtOutput["state"] = "normal"
        result = f"{ratePerHour}\t{hoursWorked}\t{grossPay}\t\t{deduction}\t\t{netPay}\n"
        self.txtOutput.insert("end", result)
        self.txtOutput["state"] = "disabled"

SimplePayroll().mainloop()

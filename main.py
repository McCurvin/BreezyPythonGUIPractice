from breezypythongui import EasyFrame


class Calculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Simple Calculator")

        # Label and field for the input
        self.addLabel(text="Enter first number", row=0, column=0)
        self.txtNum1 = self.addIntegerField(value="", row=0, column=1)
        # Label and field for the output
        self.addLabel(text="Enter second number", row=1, column=0)
        self.txtNum2 = self.addIntegerField(value="", row=1, column=1)
        self.txtResult = self.addTextField(text="0", row=2, column=0, columnspan=2, state="readonly")


        self.addButton(text="Add", row=3, column=0, columnspan=2, command=self.sum)
        self.addButton(text="Multiply", row=3, column=1, columnspan=2, command=self.multiply)
        self.addButton(text="Divide", row=4, column=0, columnspan=2, command=self.intDiv)
        self.addButton(text="Float", row=4, column=1, columnspan=2, command=self.floatDiv)
        self.addButton(text="Modulus", row=5, column=0, columnspan=2, command=self.modulus)
        self.addButton(text="Power", row=5, column=1, columnspan=2, command=self.exponent)


    def sum(self):
        num1 = self.txtNum1.getNumber()
        num2 = self.txtNum2.getNumber()
        result = num1 + num2
        self.txtResult.setText(f'The sum is {result}')

    def multiply(self):
        num1 = self.txtNum1.getNumber()
        num2 = self.txtNum2.getNumber()
        result = num1 * num2
        self.txtResult.setText(f"Result is {result}")
    def intDiv(self):
        num1 = self.txtNum1.getNumber()
        num2 = self.txtNum2.getNumber()
        result = num1 // num2
        self.txtResult.setText(f"Result is {result}")
    def floatDiv(self):
        num1 = self.txtNum1.getNumber()
        num2 = self.txtNum2.getNumber()
        result = num1 / num2
        self.txtResult.setText(f"Result is {result}")
    def modulus(self):
        num1 = self.txtNum1.getNumber()
        num2 = self.txtNum2.getNumber()
        result = num1 % num2
        self.txtResult.setText(f"Result is {result}")
    def exponent(self):
        num1 = self.txtNum1.getNumber()
        num2 = self.txtNum2.getNumber()
        result = num1 ** num2
        self.txtResult.setText(f"Result is {result}")




Calculator().mainloop()
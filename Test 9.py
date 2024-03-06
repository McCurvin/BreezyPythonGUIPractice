from breezypythongui import EasyFrame
class Calculator(EasyFrame):
    def __init__(self):
         # Create the main frame
        EasyFrame.__init__(self, "Panel Demo - v2")
         # Create the nested frame for the data panel
        dataPanel = self.addPanel(row=0,column=0,background="blue")

         # Create and add widgets to the data panel
        dataPanel.addLabel(text="Enter first number",row=0,column=0,background="blue",foreground="white")
        dataPanel.addTextField(text="0",row=0,column=1)
        dataPanel.addLabel(text="Enter second number",row=1,column=0,background="blue",foreground="white")
        dataPanel.addTextField(text="0",row=1,column=1)


         # Create the nested frame for the button panel
        buttonPanel=self.addPanel(row=1,column=0,background="black")


         # Create and add buttons to the button panel
        buttonPanel.addButton(text="+",row=0,column=0)
        buttonPanel.addButton(text="-",row=0,column=1)
        buttonPanel.addButton(text="*",row=0,column=2)
        buttonPanel.addButton(text="/",row=0,column=3)

Calculator().mainloop()
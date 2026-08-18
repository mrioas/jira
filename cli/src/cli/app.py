import toga
from toga.style.pack import *
import cli.jira.jira as jr

def Operation(number):

    iff = []
    number = int(number)

    if number%2==0:

        iff.append("Numero divisible y resultado par real")

    else:

        iff.append("No Divisible entre si")

    if number==0:

        iff.append("sayi=0")
        iff.append("Asal degil")


    elif number<0:

        iff.append("sayi<0")
        iff.append("Asal degil")

    else:

        iff.append("sayi>0")

        kn = 0
        for i in range(2,number):

            if number%i==0:

                kn=1
                break

        if kn==1:

            iff.append("Asal degil")

        else:

            if number==1:

                iff.append("Number One")

            iff.append("Adiccion")

    return iff

def from_jira(): 
    data = []
    data = jr.get_issues()
    return data

def build(app):

    ticket = toga.Box()
    create_ticket  = toga.Box()
    
    name_label = toga.Label('Descripcion de ticket: ', style=Pack(text_align=LEFT))
    name_input = toga.TextInput()
    
    run_label = toga.Label("", style=Pack(text_align=LEFT))
    run_label_1 = toga.Label("", style=Pack(text_align=LEFT))
    run_label_2 = toga.Label("", style=Pack(text_align=LEFT))

    def button(widget):

        iff = Operation(name_input.value)

        stra = "1-) " + iff[0]
        strb = "2-) " + iff[1]
        strc = "3-) " + iff[2]

        run_label.text = stra
        run_label_1.text = strb
        run_label_2.text = strc
  
    button = toga.Button('Run', on_press=button)
    button.style.padding = 20
    button.style.flex = 20

    name_label.style.update(width=100, padding_left=10)
    name_input.style.update(width=100, padding_top=10, padding_left=10)

    run_label.style.update(width=100, padding_top=10, padding_left=10)
    run_label_1.style.update(width=100, padding_top=10, padding_left=10)
    run_label_2.style.update(width=100, padding_top=10, padding_left=10)

    create_ticket.add(name_label)
    create_ticket.add(name_input)
    
    create_ticket.add(run_label)
    create_ticket.add(run_label_1)
    create_ticket.add(run_label_2)
    create_ticket.add(button)
    
    create_ticket.style.update(direction=COLUMN, width=100, padding_top=10)
    

    
    name_label_ticket = toga.Label('Lista de tickets creados por $USER:  en fecha: $DATETIME', style=Pack(text_align=LEFT))
    ticket.add(name_label_ticket) 
    container = toga.OptionContainer(
        content=[
            ("Lista de tickets", ticket), 
            ("Crear Ticket", create_ticket, toga.Icon("ticket"))
        ]
    )
    config = toga.Box()
    container.content.append("Config", config)

    return container

def main():
    #from_jira()
    return toga.App('Ticketing', 'com.app.cli', startup=build)
    #return toga.App('Tickting', 'com.app', startup=lifecycle)
    #pizza = toga.Box()
    #pasta = toga.Box()

    # Create 2 initial tabs; one with an icon, and one without.
    #container = toga.OptionContainer(
    #    content=[("Pizza", pizza), ("Pasta", pasta, toga.Icon("pasta"))]
    #)

    # Add another tab of content, without an icon.
    #salad = toga.Box()
    #container.content.append("Salad", salad)

    # Add another tab of content, with an icon
    #icecream = toga.Box()
    #container.content.append("Ice Cream", icecream, toga.Icon("icecream")

if __name__ == '__main__':
   main().main_loop()

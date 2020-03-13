from mycroft import MycroftSkill, intent_file_handler


class OrderPizza(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pizza.order.intent')
    def handle_pizza_order(self, message):
        self.speak_dialog('pizza.order')


def create_skill():
    return OrderPizza()


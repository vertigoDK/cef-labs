from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        self.result_label = Label(text="0", font_size=32)  # Место для отображения результата

        # Текстовые поля для ввода чисел
        self.num1_input = TextInput(font_size=32, multiline=False, input_filter='float')  # Первый ввод
        self.num2_input = TextInput(font_size=32, multiline=False, input_filter='float')  # Второй ввод

        # Кнопки операций
        self.add_button = Button(text="+", font_size=32)
        self.subtract_button = Button(text="-", font_size=32)
        self.multiply_button = Button(text="*", font_size=32)
        self.divide_button = Button(text="/", font_size=32)

        # Связываем кнопки с действиями
        self.add_button.bind(on_press=self.add)
        self.subtract_button.bind(on_press=self.subtract)
        self.multiply_button.bind(on_press=self.multiply)
        self.divide_button.bind(on_press=self.divide)

        # Компоновка виджетов
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(self.result_label)

        # Ввод чисел
        input_layout = BoxLayout(orientation='horizontal', spacing=10)
        input_layout.add_widget(self.num1_input)
        input_layout.add_widget(self.num2_input)
        layout.add_widget(input_layout)

        # Кнопки операций
        button_layout = BoxLayout(orientation='horizontal', spacing=10)
        button_layout.add_widget(self.add_button)
        button_layout.add_widget(self.subtract_button)
        button_layout.add_widget(self.multiply_button)
        button_layout.add_widget(self.divide_button)
        layout.add_widget(button_layout)

        return layout

    # Обработчики для арифметических операций
    def add(self, instance):
        num1 = float(self.num1_input.text) if self.num1_input.text else 0
        num2 = float(self.num2_input.text) if self.num2_input.text else 0
        self.result_label.text = str(num1 + num2)

    def subtract(self, instance):
        num1 = float(self.num1_input.text) if self.num1_input.text else 0
        num2 = float(self.num2_input.text) if self.num2_input.text else 0
        self.result_label.text = str(num1 - num2)

    def multiply(self, instance):
        num1 = float(self.num1_input.text) if self.num1_input.text else 0
        num2 = float(self.num2_input.text) if self.num2_input.text else 0
        self.result_label.text = str(num1 * num2)

    def divide(self, instance):
        num1 = float(self.num1_input.text) if self.num1_input.text else 0
        num2 = float(self.num2_input.text) if self.num2_input.text else 0
        if num2 != 0:
            self.result_label.text = str(num1 / num2)
        else:
            self.result_label.text = "Ошибка: деление на 0"

# Запуск приложения
if __name__ == '__main__':
    CalculatorApp().run()
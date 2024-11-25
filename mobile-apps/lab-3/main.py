from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout

# Статичные курсы валют
EXCHANGE_RATES = {
    "USD": 1.0,  # Курс USD к самому себе
    "EUR": 0.93,  # Курс EUR к USD
    "GBP": 0.82,  # Курс GBP к USD
    "INR": 82.65,  # Курс INR к USD
    "JPY": 148.56,  # Курс JPY к USD
    "AUD": 1.53  # Курс AUD к USD
}


class CurrencyConverterApp(App):
    def build(self):
        # Основной layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Ввод суммы
        self.amount_input = TextInput(hint_text="Введите сумму", font_size=32, multiline=False)
        self.layout.add_widget(self.amount_input)

        # Создание выпадающего списка для валют
        self.dropdown = DropDown()
        self.currencies = list(EXCHANGE_RATES.keys())  # Список доступных валют
        self.selected_currency = "USD"  # Валюта по умолчанию

        for currency in self.currencies:
            btn = Button(text=currency, size_hint_y=None, height=44)
            btn.bind(on_release=self.select_currency)
            self.dropdown.add_widget(btn)

        self.currency_button = Button(text="Выберите валюту", size_hint_y=None, height=44)
        self.currency_button.bind(on_release=self.dropdown.open)
        self.layout.add_widget(self.currency_button)

        # Метка для отображения результата
        self.result_label = Label(text="Результат: ", font_size=32)
        self.layout.add_widget(self.result_label)

        # Кнопка для выполнения конвертации
        self.convert_button = Button(text="Конвертировать", font_size=32)
        self.convert_button.bind(on_press=self.convert_currency)
        self.layout.add_widget(self.convert_button)

        return self.layout

    def select_currency(self, instance):
        """Обработчик выбора валюты"""
        self.selected_currency = instance.text
        self.currency_button.text = f"Валюта: {self.selected_currency}"

    def convert_currency(self, instance):
        """Обработчик для конвертации валюты"""
        amount = self.amount_input.text
        if not amount.isdigit():
            self.result_label.text = "Ошибка: введите корректную сумму!"
            return

        amount = float(amount)
        rate = self.get_exchange_rate(self.selected_currency)
        if rate:
            result = amount * rate
            self.result_label.text = f"Результат: {result:.2f} {self.selected_currency}"
        else:
            self.result_label.text = "Ошибка: не удалось получить курс!"

    def get_exchange_rate(self, currency):
        """Получение курса валюты из статического словаря"""
        return EXCHANGE_RATES.get(currency, None)

# Запуск приложения
if __name__ == '__main__':
    CurrencyConverterApp().run()
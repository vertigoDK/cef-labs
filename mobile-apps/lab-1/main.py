from kivy.app import App
from kivy.uix.button import Button  # Виджет кнопки
from kivy.uix.boxlayout import BoxLayout  # Для компоновки элементов
from kivy.uix.label import Label  # Виджет для текста

class MyApp(App):
    def build(self):
        # Основной компоновщик
        layout = BoxLayout(orientation='vertical')

        # Текстовый виджет
        self.label = Label(text="Привет, мир!")

        # Кнопка
        btn = Button(text="Нажми меня")
        btn.bind(on_press=self.change_text)

        # Добавляем виджеты в компоновщик
        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def change_text(self, instance):
        self.label.text = "Привет, Kivy!"

# Запуск приложения
if __name__ == '__main__':
    MyApp().run()


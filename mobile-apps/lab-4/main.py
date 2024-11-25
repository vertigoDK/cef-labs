from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.animation import Animation

class TimerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Ввод времени
        self.time_input = TextInput(hint_text="Введите время в секундах", font_size=32, multiline=False)
        self.layout.add_widget(self.time_input)

        # Метка для отображения времени
        self.time_label = Label(text="00:00", font_size=64)
        self.layout.add_widget(self.time_label)

        # Кнопка старта
        self.start_button = Button(text="Запустить таймер", font_size=32, size_hint=(1, 0.2))
        self.start_button.bind(on_press=self.start_timer)
        self.layout.add_widget(self.start_button)

        # Переменная для отсчёта времени
        self.time_left = 0
        self.is_running = False

        return self.layout

    def start_timer(self, instance):
        """Запуск таймера с анимацией"""
        if self.is_running:
            return  # Если таймер уже работает, ничего не делаем

        # Получаем время из текстового поля
        try:
            self.time_left = int(self.time_input.text)
        except ValueError:
            self.time_label.text = "Ошибка! Введите число."
            return

        self.is_running = True
        self.start_button.text = "Остановить"
        self.start_button.background_color = (1, 0, 0, 1)  # Красный цвет

        # Анимация изменения цвета кнопки
        anim = Animation(background_color=(0, 1, 0, 1), duration=self.time_left)  # Зеленый цвет
        anim.start(self.start_button)

        # Запуск таймера
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        """Обновление времени"""
        if self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.time_label.text = f"{minutes:02}:{seconds:02}"
        else:
            self.stop_timer()

    def stop_timer(self):
        """Остановка таймера"""
        self.is_running = False
        self.start_button.text = "Запустить таймер"
        self.start_button.background_color = (0, 0, 1, 1)  # Синий цвет
        Clock.unschedule(self.update_timer)

# Запуск приложения
if __name__ == '__main__':
    TimerApp().run()

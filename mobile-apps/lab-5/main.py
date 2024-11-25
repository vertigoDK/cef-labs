from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.boxlayout import BoxLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Настройки", on_press=self.go_to_settings)
        self.add_widget(btn)

    def go_to_settings(self, instance):
        self.manager.current = "settings_screen"  # Переключаемся на экран настроек

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")

        # Создаем ColorPicker для выбора цвета фона
        self.color_picker = ColorPicker()
        layout.add_widget(self.color_picker)

        # Кнопка для применения выбранного цвета
        btn_apply = Button(text="Применить", on_press=self.apply_color)
        layout.add_widget(btn_apply)

        # Кнопка для возврата в главное меню
        btn_back = Button(text="Вернуться в меню", on_press=self.go_back)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def apply_color(self, instance):
        """Применить выбранный цвет фона на главный экран"""
        selected_color = self.color_picker.color
        self.manager.get_screen("main_screen").background_color = selected_color  # Передаем цвет на главный экран

    def go_back(self, instance):
        self.manager.current = "main_screen"  # Переключаемся обратно на главный экран

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # Добавляем экраны в ScreenManager
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(SettingsScreen(name="settings_screen"))

        return sm

if __name__ == "__main__":
    MyApp().run()
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyFormApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Заголовок
        layout.add_widget(Label(text='Введите ваше имя:', font_size=20))

        # Поле ввода имени
        self.name_input = TextInput(multiline=False)
        layout.add_widget(self.name_input)

        # Кнопка "Отправить"
        button = Button(text='Отправить', font_size=18)
        button.bind(on_press=self.submit)
        layout.add_widget(button)

        return layout

    def submit(self, instance):
        name = self.name_input.text
        if name:
            print(f'Привет, {name}!')
            self.name_input.text = ''  # Очистить поле ввода
        else:
            print('Пожалуйста, введите имя.')

if __name__ == '__main__':
    MyFormApp().run()
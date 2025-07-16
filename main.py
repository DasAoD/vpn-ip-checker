from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import urllib.request


class IPBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=50, spacing=20, **kwargs)
        self.ip_label = Label(text='IP wird geladen...', font_size=32, color=(1,1,1,1))
        self.status_label = Label(text='', font_size=64)
        self.add_widget(self.status_label)
        self.add_widget(self.ip_label)
        self.refresh_ip()
        Clock.schedule_interval(lambda dt: self.refresh_ip(), 60)

    def refresh_ip(self):
        try:
            with urllib.request.urlopen("https://www.uliana.de/IP", timeout=5) as response:
                ip = response.read().decode().strip()
                self.ip_label.text = ip
                if ip == "37.221.193.70":
                    self.status_label.text = "🔒"
                    self.status_label.color = (0, 1, 0, 1)  # Grün
                else:
                    self.status_label.text = "🔓"
                    self.status_label.color = (1, 0.3, 0.3, 1)  # Rot
        except Exception as e:
            self.ip_label.text = f"Fehler: {e}"
            self.status_label.text = "❌"
            self.status_label.color = (1, 1, 0, 1)  # Gelb


class VPNIPApp(App):
    def build(self):
        self.title = "VPN IP Checker"
        return IPBox()

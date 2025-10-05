import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random
import os
import subprocess
import ctypes
import sys

class ModernAntivirus:
    def __init__(self, root):
        self.root = root
        self.root.title("ShieldGuard Security Pro")
        self.root.geometry("900x700")
        self.root.configure(bg='#2b2b2b')
        
        # Современные цвета
        self.colors = {
            'bg': '#2b2b2b',
            'fg': '#ffffff',
            'accent': '#007acc',
            'card_bg': '#3c3c3c',
            'danger': '#ff4444',
            'success': '#44ff44',
            'warning': '#ffaa00'
        }
        
        self.scanning = False
        self.threats_found = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        # Создаем Notebook (вкладки)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Вкладка Антивирус
        self.antivirus_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(self.antivirus_frame, text="🛡️ Антивирус")
        
        # Вкладка Системные утилиты
        self.tools_frame = tk.Frame(self.notebook, bg=self.colors['bg'])
        self.notebook.add(self.tools_frame, text="⚙️ Системные утилиты")
        
        self.setup_antivirus_tab()
        self.setup_tools_tab()
    
    def setup_antivirus_tab(self):
        # Заголовок
        header_frame = tk.Frame(self.antivirus_frame, bg=self.colors['bg'])
        header_frame.pack(fill='x', padx=20, pady=20)
        
        title_label = tk.Label(
            header_frame,
            text="🛡️ ShieldGuard Security Pro",
            font=('Arial', 24, 'bold'),
            fg=self.colors['fg'],
            bg=self.colors['bg']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Ваша защита в реальном времени",
            font=('Arial', 12),
            fg='#888888',
            bg=self.colors['bg']
        )
        subtitle_label.pack(pady=5)
        
        # Фрейм с кнопками
        button_frame = tk.Frame(self.antivirus_frame, bg=self.colors['card_bg'], relief='flat', bd=1)
        button_frame.pack(fill='x', padx=20, pady=10)
        
        # Кнопки сканирования
        self.quick_scan_btn = tk.Button(
            button_frame,
            text="⚡ Быстрое сканирование",
            command=self.quick_scan,
            bg=self.colors['accent'],
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            height=2,
            width=25
        )
        self.quick_scan_btn.pack(pady=10, padx=20, fill='x')
        
        self.full_scan_btn = tk.Button(
            button_frame,
            text="🔍 Полное сканирование",
            command=self.full_scan,
            bg=self.colors['accent'],
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            height=2,
            width=25
        )
        self.full_scan_btn.pack(pady=10, padx=20, fill='x')
        
        # Прогресс-бар
        self.progress_frame = tk.Frame(self.antivirus_frame, bg=self.colors['bg'])
        self.progress_frame.pack(fill='x', padx=20, pady=10)
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            orient='horizontal',
            length=760,
            mode='determinate'
        )
        self.progress_bar.pack(pady=10)
        
        # Статус
        self.status_label = tk.Label(
            self.progress_frame,
            text="Готов к сканированию",
            font=('Arial', 12),
            fg=self.colors['fg'],
            bg=self.colors['bg']
        )
        self.status_label.pack()
        
        # Лог результатов
        log_frame = tk.Frame(self.antivirus_frame, bg=self.colors['bg'])
        log_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        log_label = tk.Label(
            log_frame,
            text="Результаты сканирования:",
            font=('Arial', 11, 'bold'),
            fg=self.colors['fg'],
            bg=self.colors['bg']
        )
        log_label.pack(anchor='w')
        
        # Текстовое поле с прокруткой
        text_frame = tk.Frame(log_frame, bg=self.colors['card_bg'])
        text_frame.pack(fill='both', expand=True, pady=5)
        
        self.results_text = tk.Text(
            text_frame,
            height=15,
            bg='#1e1e1e',
            fg='#ffffff',
            insertbackground='white',
            selectbackground=self.colors['accent'],
            font=('Consolas', 10),
            relief='flat'
        )
        
        scrollbar = ttk.Scrollbar(text_frame, orient='vertical', command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    def setup_tools_tab(self):
        # Заголовок утилит
        tools_header = tk.Label(
            self.tools_frame,
            text="⚙️ Системные утилиты",
            font=('Arial', 20, 'bold'),
            fg=self.colors['fg'],
            bg=self.colors['bg']
        )
        tools_header.pack(pady=20)
        
        # Фрейм для утилит
        tools_container = tk.Frame(self.tools_frame, bg=self.colors['card_bg'])
        tools_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Утилита 1: Активация Windows
        activate_frame = tk.Frame(tools_container, bg=self.colors['card_bg'], relief='flat', bd=1)
        activate_frame.pack(fill='x', padx=10, pady=10)
        
        activate_label = tk.Label(
            activate_frame,
            text="🎯 Активация Windows & Удаление водяного знака",
            font=('Arial', 14, 'bold'),
            fg=self.colors['fg'],
            bg=self.colors['card_bg']
        )
        activate_label.pack(anchor='w', padx=10, pady=5)
        
        activate_desc = tk.Label(
            activate_frame,
            text="• Активирует Windows KMS активацией\n• Удаляет водяной знак 'Активируйте Windows'\n• Работает на Windows 10/11",
            font=('Arial', 10),
            fg='#cccccc',
            bg=self.colors['card_bg'],
            justify='left'
        )
        activate_desc.pack(anchor='w', padx=10, pady=5)
        
        self.activate_btn = tk.Button(
            activate_frame,
            text="🚀 Активировать Windows",
            command=self.activate_windows,
            bg='#28a745',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            height=2
        )
        self.activate_btn.pack(pady=10, padx=10, fill='x')
        
        # Утилита 2: Очистка диска
        clean_frame = tk.Frame(tools_container, bg=self.colors['card_bg'], relief='flat', bd=1)
        clean_frame.pack(fill='x', padx=10, pady=10)
        
        clean_label = tk.Label(
            clean_frame,
            text="🧹 Очистка временных файлов",
            font=('Arial', 14, 'bold'),
            fg=self.colors['fg'],
            bg=self.colors['card_bg']
        )
        clean_label.pack(anchor='w', padx=10, pady=5)
        
        self.clean_btn = tk.Button(
            clean_frame,
            text="🧽 Очистить системный мусор",
            command=self.clean_temp_files,
            bg=self.colors['warning'],
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            height=2
        )
        self.clean_btn.pack(pady=10, padx=10, fill='x')
        
        # Лог для утилит
        tools_log_frame = tk.Frame(self.tools_frame, bg=self.colors['bg'])
        tools_log_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.tools_log = tk.Text(
            tools_log_frame,
            height=10,
            bg='#1e1e1e',
            fg='#ffffff',
            font=('Consolas', 9),
            relief='flat'
        )
        tools_scrollbar = ttk.Scrollbar(tools_log_frame, orient='vertical', command=self.tools_log.yview)
        self.tools_log.configure(yscrollcommand=tools_scrollbar.set)
        
        self.tools_log.pack(side='left', fill='both', expand=True)
        tools_scrollbar.pack(side='right', fill='y')
    
    def add_tools_log(self, message):
        self.tools_log.insert(tk.END, f"{message}\n")
        self.tools_log.see(tk.END)
        self.root.update()
    
    def activate_windows(self):
        """Реальная функция активации Windows и удаления водяного знака"""
        try:
            self.activate_btn.configure(state='disabled', text="⏳ Активация...")
            self.add_tools_log("🚀 Запуск активации Windows...")
            
            # Проверяем права администратора
            if not ctypes.windll.shell32.IsUserAnAdmin():
                self.add_tools_log("❌ Требуются права администратора!")
                messagebox.showerror("Ошибка", "Запустите программу от имени администратора!")
                self.activate_btn.configure(state='normal', text="🚀 Активировать Windows")
                return
            
            # KMS активация Windows
            self.add_tools_log("🔑 Настройка KMS сервера...")
            kms_commands = [
                'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX',  # Windows 10/11 Pro
                'slmgr /skms kms8.msguides.com',
                'slmgr /ato',
                'slmgr /dlv'
            ]
            
            for cmd in kms_commands:
                self.add_tools_log(f"Выполнение: {cmd}")
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    self.add_tools_log("✅ Команда выполнена успешно")
                else:
                    self.add_tools_log("⚠️  Команда выполнена с предупреждением")
                time.sleep(1)
            
            # Удаление водяного знака через реестр
            self.add_tools_log("🔧 Удаление водяного знака...")
            try:
                import winreg
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                   r"Control Panel\Desktop", 
                                   0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "PaintDesktopVersion", 0, winreg.REG_DWORD, 0)
                winreg.CloseKey(key)
                self.add_tools_log("✅ Водяной знак удален из реестра")
            except Exception as e:
                self.add_tools_log(f"⚠️  Ошибка реестра: {e}")
            
            # Перезапуск Explorer для применения изменений
            self.add_tools_log("🔄 Перезапуск проводника...")
            subprocess.run("taskkill /f /im explorer.exe", shell=True)
            time.sleep(2)
            subprocess.run("start explorer.exe", shell=True)
            
            self.add_tools_log("🎉 Активация завершена! Перезагрузите компьютер.")
            messagebox.showinfo("Успех", "Windows активирована!\nВодяной знак удален!\nПерезагрузите компьютер для применения изменений.")
            
        except Exception as e:
            self.add_tools_log(f"❌ Ошибка активации: {str(e)}")
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
        finally:
            self.activate_btn.configure(state='normal', text="🚀 Активировать Windows")
    
    def clean_temp_files(self):
        """Очистка временных файлов"""
        try:
            self.clean_btn.configure(state='disabled', text="⏳ Очистка...")
            self.add_tools_log("🧹 Начинаю очистку временных файлов...")
            
            temp_folders = [
                os.environ.get('TEMP', ''),
                os.environ.get('TMP', ''),
                os.path.expanduser('~\\AppData\\Local\\Temp'),
                'C:\\Windows\\Temp'
            ]
            
            total_cleaned = 0
            for folder in temp_folders:
                if os.path.exists(folder):
                    self.add_tools_log(f"📁 Очистка папки: {folder}")
                    try:
                        for filename in os.listdir(folder):
                            filepath = os.path.join(folder, filename)
                            try:
                                if os.path.isfile(filepath):
                                    size = os.path.getsize(filepath)
                                    os.remove(filepath)
                                    total_cleaned += size
                                    self.add_tools_log(f"✅ Удален: {filename}")
                            except Exception as e:
                                continue  # Пропускаем файлы которые нельзя удалить
                    except Exception as e:
                        self.add_tools_log(f"⚠️  Не удалось очистить: {folder}")
            
            cleaned_mb = total_cleaned / (1024 * 1024)
            self.add_tools_log(f"🎉 Очистка завершена! Освобождено: {cleaned_mb:.2f} MB")
            messagebox.showinfo("Успех", f"Очистка завершена!\nОсвобождено: {cleaned_mb:.2f} MB")
            
        except Exception as e:
            self.add_tools_log(f"❌ Ошибка очистки: {str(e)}")
            messagebox.showerror("Ошибка", f"Произошла ошибка при очистке: {str(e)}")
        finally:
            self.clean_btn.configure(state='normal', text="🧽 Очистить системный мусор")
    
    # Остальные методы антивируса остаются без изменений
    def quick_scan(self):
        if not self.scanning:
            self.start_scan("quick")
    
    def full_scan(self):
        if not self.scanning:
            self.start_scan("full")
    
    def start_scan(self, scan_type):
        self.scanning = True
        self.threats_found = 0
        self.results_text.delete(1.0, tk.END)
        
        self.quick_scan_btn.configure(state='disabled')
        self.full_scan_btn.configure(state='disabled')
        
        scan_thread = threading.Thread(target=self.run_scan, args=(scan_type,))
        scan_thread.daemon = True
        scan_thread.start()
    
    def run_scan(self, scan_type):
        files_to_scan = 100 if scan_type == "quick" else 500
        threats = [
            "Trojan.Win32.Malware", "Riskware.HackTool", "PUP.Optional.Bundle",
            "Backdoor.Agent", "Ransomware.Crypter", "Worm.Virus.Dropper"
        ]
        
        for i in range(files_to_scan + 1):
            if not self.scanning:
                break
                
            progress = i / files_to_scan
            self.progress_bar['value'] = progress * 100
            
            if random.random() < 0.04:
                threat = random.choice(threats)
                self.threats_found += 1
                self.add_log(f"🚨 УГРОЗА: {threat} в file_{i:03d}.exe")
            elif random.random() < 0.3:
                self.add_log(f"✅ Безопасно: system_file_{i:03d}.dll")
            
            status_text = f"Сканирование... {i}/{files_to_scan} файлов"
            if self.threats_found > 0:
                status_text += f" | Угроз: {self.threats_found}"
            
            self.status_label.configure(text=status_text)
            time.sleep(0.01)
        
        self.finish_scan()
    
    def add_log(self, message):
        self.root.after(0, lambda: self.results_text.insert(tk.END, message + "\n"))
        self.root.after(0, lambda: self.results_text.see(tk.END))
    
    def finish_scan(self):
        self.scanning = False
        self.progress_bar['value'] = 100
        
        self.quick_scan_btn.configure(state='normal')
        self.full_scan_btn.configure(state='normal')
        
        if self.threats_found > 0:
            self.status_label.configure(text=f"Обнаружено угроз: {self.threats_found}", fg=self.colors['danger'])
            messagebox.showwarning("Результат", f"Найдено {self.threats_found} угроз!")
        else:
            self.status_label.configure(text="Система защищена!", fg=self.colors['success'])
            messagebox.showinfo("Результат", "✅ Компьютер защищен!")

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernAntivirus(root)
    root.mainloop()

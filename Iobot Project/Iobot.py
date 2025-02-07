import customtkinter as ctk
import random
import threading
from gtts import gTTS
import playsound
import speech_recognition as sr
import time
import datetime
import tkinter as tk
from tkinter import filedialog





# ========================================= Setting Window ================================================ #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
waktu_terkini = datetime.datetime.now().strftime('%H:%M')
window = ctk.CTk()
window.title("Iobot.ai")
window.geometry("700x580+460+55")
window.resizable(False, False)
# ===================================== Setting Window - Closed ============================================ #





# ============================================ Membership ================================================= #
class PaketApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.window = ctk.CTk()
        self.window.resizable(0,0)
        self.window.geometry("760x450")
        self.window.title("Paket Anda")
        self.title_label = ctk.CTkLabel(self.window, text="Tingkatkan paket Anda", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=(20, 10))
        self.tab_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.tab_frame.pack(pady=(0, 20))
        self.pribadi_button = ctk.CTkButton(self.tab_frame, text="Pribadi", width=80, state="normal")
        self.pribadi_button.grid(row=0, column=0, padx=10)
        self.bisnis_button = ctk.CTkButton(self.tab_frame, text="Bisnis", width=80, state="normal")
        self.bisnis_button.grid(row=0, column=1, padx=10)
        self.cards_frame = ctk.CTkFrame(self.window)
        self.cards_frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.free_card = ctk.CTkFrame(self.cards_frame, width=200, height=350, corner_radius=15)
        self.free_card.grid(row=0, column=0, padx=10, pady=10, sticky="n")
        self.free_title = ctk.CTkLabel(self.free_card, text="Free", font=("Arial", 18, "bold"))
        self.free_title.pack(pady=(20, 5))
        self.free_price = ctk.CTkLabel(self.free_card, text="$0 USD/bulan", font=("Arial", 16))
        self.free_price.pack(pady=(0, 20))
        self.free_desc = ctk.CTkLabel(self.free_card, text="\nJelajahi bagaimana AI dapat membantu Anda\n dengan tugas sehari-hari", font=("Arial", 12), justify="center")
        self.free_desc.pack(pady=(0, 20))
        self.free_button = ctk.CTkButton(self.free_card, text="Paket Anda saat ini", state="disabled")
        self.free_button.pack(pady=(0, 20))
        self.plus_card = ctk.CTkFrame(self.cards_frame, width=200, height=350, corner_radius=15, fg_color="#1c2b3a")
        self.plus_card.grid(row=0, column=1, padx=10, pady=10, sticky="n")
        self.plus_title = ctk.CTkLabel(self.plus_card, text="Plus", font=("Arial", 18, "bold"))
        self.plus_title.pack(pady=(20, 5))
        self.popular_label = ctk.CTkLabel(self.plus_card, text="POPULER", font=("Arial", 10), fg_color="green", text_color="white", corner_radius=10, width=80)
        self.popular_label.pack(pady=(0, 10))
        self.plus_price = ctk.CTkLabel(self.plus_card, text="$20 USD/bulan", font=("Arial", 16))
        self.plus_price.pack(pady=(0, 20))
        self.plus_desc = ctk.CTkLabel(self.plus_card, text="\nTingkatkan produktivitas dan kreativitas\n dengan akses lebih luas", font=("Arial", 12), justify="center")
        self.plus_desc.pack(pady=(0, 20))
        self.plus_button = ctk.CTkButton(self.plus_card, text="Dapatkan Plus")
        self.plus_button.pack(pady=(0, 20))
        self.pro_card = ctk.CTkFrame(self.cards_frame, width=200, height=350, corner_radius=15)
        self.pro_card.grid(row=0, column=2, padx=10, pady=10, sticky="n")
        self.pro_title = ctk.CTkLabel(self.pro_card, text="Pro", font=("Arial", 18, "bold"))
        self.pro_title.pack(pady=(20, 5))
        self.pro_price = ctk.CTkLabel(self.pro_card, text="$200 USD/bulan", font=("Arial", 16))
        self.pro_price.pack(pady=(0, 20))
        self.pro_desc = ctk.CTkLabel(self.pro_card, text="\nManfaatkan OpenAI dengan level akses\n tertinggi", font=("Arial", 12), justify="center")
        self.pro_desc.pack(pady=(0, 20))
        self.pro_button = ctk.CTkButton(self.pro_card, text="Dapatkan Pro")
        self.pro_button.pack(pady=(0, 20))
    def run(self):
        self.window.mainloop()
# ============================================= Membership - Close ======================================= #





# ============================================== About Us App ============================================ #
class AboutUsApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.resizable(0,0)
        self.window.title("About IoBot.AI")
        self.window.geometry("850x400")
        ctk.set_appearance_mode("dark")
        self.about_frame = ctk.CTkFrame(self.window, width=560, height=450, corner_radius=20, border_color="gray")
        self.about_frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.title_label = ctk.CTkLabel(self.about_frame, text="Iobot.AI", font=("Arial", 24, "bold"), text_color="white")
        self.title_label.pack(pady=15)
        self.description = """
                                                                            ✨ **Kenali Iobot: Asisten AI Cerdas Anda!** ✨
        
        Bayangkan memiliki asisten pribadi yang **selalu siap**, **selalu belajar**, dan **selalu berkembang** sesuai kebutuhan Anda. 
        Inilah **Iobot**, chatbot canggih yang didesain khusus untuk memberikan pengalaman percakapan yang lebih interaktif, fleksibel, dan intuitif!
                                                                    Dibuat oleh Bio, seorang mahasiswa SarMag Gunadarma
        
        🔹 **Desain Dinamis & Interaktif** – Iobot hadir dengan **navbar yang bisa diseret**
        🔹 **Penyimpanan Percakapan** – Tidak perlu khawatir kehilangan informasi!
        🔹 **Tema yang Dapat Disesuaikan** – Sesuaikan tampilan Iobot dengan **tema gelap atau terang**.
        🔹 **Respon AI Berbasis Kamus Percakapan** – Semakin sering digunakan, semakin pintar Iobot.
        🔹 **Pencarian Percakapan Cepat** – Temukan percakapan lama hanya dengan beberapa ketukan.
        🔹 **Fitur Premium untuk Pengalaman Lebih Baik** – Dapatkan fitur eksklusif dengan **upgrade ke versi premium**
        
                                                                                  **Iobot bukan sekadar chatbot biasa**
                                ia adalah solusi cerdas yang membantu Anda berkomunikasi lebih efektif, efisien, dan menyenangkan. 
                                                                                        Saatnya berinteraksi dengan
                                                                            **AI yang benar-benar memahami Anda!** 🚀
"""
        self.description_label = ctk.CTkLabel(self.about_frame, text=self.description, font=("Arial", 12), anchor="w", justify="left", text_color="lightgray")
        self.description_label.pack(padx=20, pady=10)
    def run(self):
        self.window.mainloop()
# ======================================== AboutUs App - Close ============================================= #





# ============================================= Data IoBot ===================================================#
responses = {
        "halo":['Hai...Nama saya adalah Iobot.Senang bertemu denganmu...',
                'Hai...Namaku iobot.Ada yang bisa saya bantu?',
                'Hai...Namaku iobot,biasanya dipanggil si robot.Senang bertemu denganmu'],
        'kabar':['Terimakasih atas perhatiannya,saya baik baik saja.Ada yang bisa saya bantu?',
                   'Baik sekali anda bertanya. Saya baik-baik saja. Walau saya robot, saya juga butuh perhatian',
                   'Saya baik-baik saja. Terimakasih sudah bertanya, apakah ada yang bisa saya bantu?'],
        'jokes':['Kenapa komputer selalu dingin?\nKarena menggunakkan "Windows" xixixi',
                 'Kenapa di Facebook banyak drama?\nKarena status aja sering "update" xixixi',
                 'Kenapa jam selalu bingung?\nKarena dia selalu berputar di tempat xixixi',
                 'Kenapa koruptor selalu memakai jas?\nKarena biar kelihatan rapih meski kotor didalam xixixi'],
        'rancang':['Saya dibuat oleh Bio calon programmer handal',
                     'Saya dibuat oleh seorang calon programmer handal namanya Bio.',
                     'Saya dirancang oleh Bio. Bio adalah seorang programmer handal.'],
        'mau':['Namanya Bio...Seorang programmer handal dan CEO GameHub... mau liat karya lainnya? bisa di cek di directory dia.'],
        'perkenalkan diri':['Perkenalkan namaku Iobot yang dirancang membantu anda',
                           'Perkenalkan namaku Iobot. Walau diriku robot, aku juga mempunyai sifat yang sama seperti manusia lohh. \nAku dirancang untuk membantu kegiatanmu sehari-hari',
                           'Perkenalkan nama saya adalah Iobot. Saya adalah seorang asisten dan saya dirancang untuk membantu anda'],
        'wkwkwk':['Hahaha...lucu ya, seneng dengarnya','Hahaha.. (ketawa karir)','Hahaha... ada yang bisa dibantu lagi?'],
        'bisa':['Saya bisa berbagai hal, kamu bisa tanya apa saja kecuali ngepel rumah',
                     'Saya bisa bantu kamu ngerjain tugas, PR, ngoding. Tapi jangan kebanyakan plss.'],
        'kurang':['Maaf yah...Ada yang bbisa saya bantu lagi?',
                  'Maaf saya sudah berusaha sekuat tenaga...',
                  'Maaf ya ga lucu...'],
        'gombal':['Kamu itu kayak Wi-Fi, karena setiap kali aku deket sama kamu, sinyal hati aku langsung penuh! Tanpa kamu, koneksi aku nggak ada artinya.😜',
                  'Kamu itu kayak kopi, deh. Semakin deket, semakin aku nggak bisa berhenti mikirin kamu. Setiap detik bersamamu, rasanya selalu pengen nambah lagi. ☕❤️',
                  'Kamu itu kayak sinar matahari, selalu bikin hari-hariku cerah! ☀️'],
        'makasih':['Seneng dengernya...Kalo ada yang mau dibantu bilang lagi ajahh...',
                   'Sama-sama! Kalau butuh bantuan lagi, tinggal bilang aja! 😄'],
        'nyanyi':['Sebagai AI, saya tidak bisa benar-benar bernyanyi, tapi saya bisa mencoba! 🎶\n🎵 Twinkle, twinkle, little star\nHow I wonder what you are...\nUp above the world so high,\nLike a diamond in the sky! ✨🎶\nAtau mungkin kamu ingin lirik lagu lain? 😆🎤',
                  'Aku nggak bisa nyanyi, tapi aku bisa kasih lirik lagu yang aku suka! Salah satunya "Imagine" dari John Lennon. Ini salah satu lagu yang penuh makna dan sering dianggap klasik:\nImagine theres no heaven\nIts easy if you try\nNo hell below us\nAbove us, only sky\nImagine all the people\nLiving for today...\n\nKalau kamu suka lagu ini, bisa coba nyanyiin bareng! Ada lagu favorit lain?',
                  'Aku nggak bisa nyanyi, tapi bayangin aja suara aku lagi merdu banget! Kalau mau, aku bisa bantu cari lirik lagu atau cerita tentang lagu yang kamu suka.\nAda lagu tertentu yang pengen kamu denger?',
                  'Sayangnya, aku lebih ahli dalam menulis lirik daripada menyanyi. Tapi, bayangin aja suara aku yang nyanyinya luar biasa!'],
        'masak':['Kamu bisa coba membuat pasta dengan saus tomat. Cukup siapkan pasta, tomat, bawang putih, dan minyak zaitun. Tumis bawang putih, tambahkan tomat, dan masukkan pasta yang sudah direbus. Campur semuanya, dan pasta siap disantap!',
                 'Kamu bisa coba sandwich dengan selai kacang dan pisang, atau buat salad dengan sayuran segar dan dressing lemon. Simple dan lezat!',
                 'Bagaimana kalau kamu membuat mie instan dengan tambahan sayuran dan telur rebus? Cepat dan tetap sehat!',
                 'Coba buat kentang panggang dengan bawang putih dan rosemary, atau kamu bisa buat mashed potato sebagai pelengkap hidangan utama!'],
        'quotes':['"The only way to do great work is to love what you do." - Steve Jobs',
                  '"Life is what happens when youre busy making other plans." - John Lennon',
                  'The best way to predict the future is to create it." - Peter Drucker',
                  '"In the middle of every difficulty lies opportunity." - Albert Einstein',
                  '"Believe you can and youre halfway there." - Theodore Roosevelt'],
        'buku':['"Atomic Habits" oleh James Clear\nBuku ini memberikan panduan praktis untuk membangun kebiasaan kecil yang bisa mengarah pada perubahan besar dalam hidup. Sangat berguna bagi siapa saja yang ingin meningkatkan produktivitas atau kesejahteraan.',
                '"The Power of Now" oleh Eckhart Tolle\nBuku ini mengajarkan kita untuk hidup di saat ini, melepaskan kekhawatiran tentang masa lalu atau masa depan, dan menemukan kedamaian dalam momen yang ada.',
                '"The Diary of a Young Girl" oleh Anne Frank\nBuku yang menyentuh tentang kehidupan seorang gadis muda Yahudi yang bersembunyi selama Perang Dunia II. Dikenal sebagai salah satu dokumen yang paling berharga tentang tragedi Holocaust.',
                '"Quiet: The Power of Introverts in a World That Cant Stop Talking" oleh Susan Cain\nBuku ini menggali kekuatan introvert di dunia yang sering kali lebih menghargai kepribadian ekstrovert, memberikan wawasan tentang bagaimana introvert bisa sukses di banyak bidang.'],
        'jam':[f'Sekarang menunjukkan pukul {waktu_terkini} WIB'],
        'pukul':[f'Sekarang menunjukkan pukul {waktu_terkini} WIB']
    }
# ============================================ Dat IoBot - Close ============================================ #






# ============================================= Input Voice User ============================================== #
def get_voice_input():
    """
    Mengambil input suara dari mikrofon pengguna dan mengonversinya menjadi teks.
    
    Returns:
        str: Teks hasil konversi suara atau pesan error jika gagal.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silakan berbicara...")
        try:
            # Mendengarkan input suara
            audio = recognizer.listen(source)
            print("Mendengarkan selesai, sedang memproses...")
            
            time.sleep(1)
            # Mengonversi suara ke teks menggunakan Google Web Speech API
            text = recognizer.recognize_google(audio, language="id-ID")
            return text
        except sr.UnknownValueError:
            print("Maaf, tidak dapat mengenali suara Anda.")
            return ""
        except sr.RequestError as e:
            print(f"Tidak dapat terhubung ke layanan pengenalan suara: {e}")
            return ""
# ========================================= Input Voice User - Close ========================================= #






# ========================================= Input process Voice ============================================== #
def process_voice(user_input):
    if __name__ == "__main__":
        user_input = get_voice_input()
    if user_input:
        data_input = user_input.strip()
        if not data_input:
            return
        chat_interface.configure(state="normal")
        chat_interface.insert("end", f"\nKamu: {data_input}\n",("user",))
        chat_interface.insert("end", "Bot sedang mengetik...\n")
        chat_interface.configure(state="disabled")
        chat_interface.see("end")
        threading.Thread(target=bot_response, args=(chat_interface, data_input)).start()
    else:
        print("Gagal mengambil input suara.")
# ======================================Input Process Voice - Close ========================================== #





# ============================================= Voice Note ================================================== #
def voice_note(text):
    tts = gTTS(text, lang="id")  
    tts.save("suara.mp3")
    time.sleep(1)
    playsound.playsound("suara.mp3")
# ======================================== Voice Note - Close ============================================ #






# ============================================= Pilih response ============================================== #
def process_bot(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Maaf, saya belum memahami itu."
# ============================================== Pilih response - Close ================================================ #






# ===================================================== Chat Iobot ==================================================== #
def bot_response(chat_interface, user_input):
    time.sleep(random.uniform(1, 2))
    response_bot = process_bot(user_input)
    chat_interface.configure(state="normal")
    chat_interface.delete("end-2l", "end")
    for char in f"\nIobot: {response_bot}\n":
        time.sleep(0.01)
        chat_interface.insert("end", char,("bot",))
        chat_interface.see("end")
        chat_interface.update()
    voice_note(response_bot)
    chat_interface.configure(state="disabled")
# ================================================ Chat Iobot - Close ==================================================== #






# ==================================================== Chat User ==================================================== #
def gettinginput(chat_interface, user_input):
    data_input = user_input.get().strip()
    if not data_input:
        return
    chat_interface.configure(state="normal")
    chat_interface.insert("end", f"\nKamu: {data_input}\n",("user",))
    chat_interface.insert("end", "Bot sedang mengetik...\n")
    chat_interface.configure(state="disabled")
    chat_interface.see("end")
    user_input.delete(0, "end")
    threading.Thread(target=bot_response, args=(chat_interface, data_input)).start()
# ================================================ Chat User - Close ==================================================== #






# ================================================ Save Chat ==================================================== #
def save_conversation(chat_interface):
    file_name = f"chat_session_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(chat_interface.get("1.0", "end"))
    tk.messagebox.showinfo("Sukses", f"Sesi percakapan disimpan sebagai {file_name}.")
# ============================================ Save Chat- Close ==================================================== #





# ================================================ Load Chat ==================================================== #
def load_conversation(chat_interface):
    file_path = filedialog.askopenfilename(
        title="Pilih File Percakapan",
        filetypes=[("Text Files", "*.txt")]
    )
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        chat_interface.configure(state="normal")
        chat_interface.delete("1.0", "end")
        chat_interface.insert("1.0", content)
        chat_interface.configure(state="disabled")
        tk.messagebox.showinfo("Sukses", "Percakapan berhasil dimuat.")
    except Exception as e:
        tk.messagebox.showinfo("Gagal", f"Terjadi kesalahan: {e}")
# ================================================ Load Chat - Close ==================================================== #





# ==================================================== Upgrade Premium ==================================================== #
def upgrade_premium():
    if __name__ == "__main__":
        app = PaketApp()
        app.run()
# ================================================ Upgrade Premium - Close ==================================================== #





# ============================================== About Us =============================================== #
def about_us():
    if __name__ == "__main__":
        app = AboutUsApp()
        app.run()
# ========================================= About Us - Close =========================================== #






# ================================================ GUI =======================================================#
frame = ctk.CTkFrame(window, corner_radius=15)
frame.pack(padx=10, pady=10, fill="both", expand=True)
# ==================== # ==================== # ==================== # ==================== #
title_label = ctk.CTkLabel(frame, text="Selamat datang di Iobot.ai!", font=("Arial", 18, "bold"))
title_label.pack(pady=10)
# ==================== # ==================== # ==================== # ==================== #
chat_frame = ctk.CTkFrame(frame, corner_radius=10)
chat_frame.pack(padx=10, pady=10, fill="both", expand=True)
# ==================== # ==================== # ==================== # ==================== #
chat_interface = ctk.CTkTextbox(chat_frame, wrap="word", state="disabled", font=("Arial", 14), spacing2=5)
chat_interface.pack(side="left", fill="both", expand=True, padx=5, pady=5)
# ==================== # ==================== # ==================== # ==================== #
scrollbar = ctk.CTkScrollbar(chat_frame, command=chat_interface.yview)
scrollbar.pack(side="right", fill="y")
# ==================== # ==================== # ==================== # ==================== #
chat_interface.configure(yscrollcommand=scrollbar.set)
# ==================== # ==================== # ==================== # ==================== #
input_frame = ctk.CTkFrame(frame, corner_radius=10)
input_frame.pack(fill="x", padx=10, pady=5)
# ==================== # ==================== # ==================== # ==================== #
user_input = ctk.CTkEntry(input_frame, placeholder_text="Ketik pesan...", width=360)
user_input.pack(side="left", padx=10, pady=10, fill="x", expand=True)
user_input.bind("<Return>", lambda event: gettinginput(chat_interface, user_input))
# ==================== # ==================== # ==================== # ==================== #
vn_button = ctk.CTkButton(input_frame, width=10,text="VN", command=lambda: process_voice(user_input))
vn_button.pack(side="right", padx=(0,10), pady=10)
# ==================== # ==================== # ==================== # ==================== #
send_button = ctk.CTkButton(input_frame, text="Kirim", command=lambda: gettinginput(chat_interface, user_input))
send_button.pack(side="right", padx=10, pady=10)
# ==================== # ==================== # ==================== # ==================== #
save_button = ctk.CTkButton(window, fg_color="#26C6DA", hover_color="#00ACC1",text="Save Chat", command=lambda: save_conversation(chat_interface))
save_button.pack(padx=28, pady=10,side='left')
# ==================== # ==================== # ==================== # ==================== #
load_button = ctk.CTkButton(window, fg_color="#1E88E5", hover_color="#1565C0",text="Load Chat", command=lambda: load_conversation(chat_interface))
load_button.pack(padx=(0,28),pady=10,side='left')
# ==================== # ==================== # ==================== # ==================== #
upgrade_premium = ctk.CTkButton(window, fg_color='#B8860B', hover_color="#DAA520",text="Upgrade Premium", command=upgrade_premium)
upgrade_premium.pack(padx=(0,28),pady=10,side='left')
# ==================== # ==================== # ==================== # ==================== #
about_button = ctk.CTkButton(window, fg_color="#66BB6A", hover_color="#388E3C", text="About Us", command=about_us)
about_button.pack(padx=(0,28),pady=10,side='left')
# ==================== # ==================== # ==================== # ==================== #
# ============================================= GUI - Close ================================================#
window.mainloop()
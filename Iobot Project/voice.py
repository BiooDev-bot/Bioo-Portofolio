import speech_recognition as sr

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

            # Mengonversi suara ke teks menggunakan Google Web Speech API
            text = recognizer.recognize_google(audio, language="id-ID")
            print(f"Anda berkata: {text}")
            return text
        except sr.UnknownValueError:
            print("Maaf, tidak dapat mengenali suara Anda.")
            return ""
        except sr.RequestError as e:
            print(f"Tidak dapat terhubung ke layanan pengenalan suara: {e}")
            return ""

# Contoh penggunaan:
if __name__ == "__main__":
    user_input = get_voice_input()
    if user_input:
        print(f"Input suara berhasil: {user_input}")
    else:
        print("Gagal mengambil input suara.")

import customtkinter as ctk

class PaketApp:
    def __init__(self):
        # Set up CTk theme and appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Window configuration
        self.window = ctk.CTk()
        self.window.geometry("760x450")
        self.window.title("Paket Anda")

        # Title label
        self.title_label = ctk.CTkLabel(self.window, text="Tingkatkan paket Anda", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=(20, 10))

        # Tab options (Pribadi, Bisnis)
        self.tab_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.tab_frame.pack(pady=(0, 20))

        self.pribadi_button = ctk.CTkButton(self.tab_frame, text="Pribadi", width=80, state="normal")
        self.pribadi_button.grid(row=0, column=0, padx=10)

        self.bisnis_button = ctk.CTkButton(self.tab_frame, text="Bisnis", width=80, state="normal")
        self.bisnis_button.grid(row=0, column=1, padx=10)

        # Pricing cards frame
        self.cards_frame = ctk.CTkFrame(self.window)
        self.cards_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Free plan card
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

        # Plus plan card
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

        # Pro plan card
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

if __name__ == "__main__":
    app = PaketApp()
    app.run()
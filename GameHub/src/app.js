document.addEventListener("alpine:init", () => {
  Alpine.data("products", () => ({
    items: [
      {
        id: 1,
        name: "Cyberpunk 2077",
        img: "cbpunk.jpg",
        page: "Game open-world, game action-adventure yang berlatar waktu malam hari, megalopolis yang tamak akan kekuatan, kekayaan, dan kecantikan tubuh.",
        price: 550.0,
      },
      {
        id: 2,
        name: "Tekken 8",
        img: "tekken8.jpg",
        page: "game pertarungan yang dikembangkan dan diterbitkan oleh Bandai Namco Entertainment. Sebagai entri terbaru dalam seri Tekken yang ikonik, Tekken 8 menawarkan pertempuran yang intens dengan grafis yang memukau dan mekanika permainan yang ditingkatkan.",
        price: 700.0,
      },
      {
        id: 3,
        name: "Valorant",
        img: "valo.jpg",
        page: "game first-person shooter (FPS) taktis yang dikembangkan dan diterbitkan oleh Riot Games. Dalam Valorant, pemain bergabung dalam tim untuk bertarung dalam pertandingan 5v5 yang intens. Setiap karakter, yang disebut memiliki kemampuan unik yang dapat mempengaruhi jalannya permainan.",
        price: 0,
      },
      {
        id: 4,
        name: "Ghost Of Tsuhisima",
        img: "703718-ghost-of-tsushima-hd-wallpaper-and-background-image.png",
        page: " game aksi petualangan yang dikembangkan oleh Sucker Punch Productions dan diterbitkan oleh Sony Interactive Entertainment. Berlatar belakang pada periode feodal Jepang, game ini mengikuti kisah Jin Sakai, seorang samurai yang berjuang untuk melindungi pulau Tsushima dari invasi Mongol. Dengan gameplay yang menggabungkan pertarungan berbasis samurai dan stealth, Ghost of Tsushima menawarkan pertempuran yang menegangkan serta eksplorasi yang mendalam dalam dunia yang indah dan terbuka.",
        price: 750.0,
      },
      {
        id: 5,
        name: "Hades",
        img: "1151800.png",
        page: "game roguelike aksi yang dikembangkan dan diterbitkan oleh Supergiant Games. Dalam Hades, pemain mengendalikan Zagreus, putra Hades, yang berusaha melarikan diri dari dunia bawah untuk mencapai Olympus. Game ini menonjol dengan mekanika permainan yang cepat dan responsif, serta desain visual yang kaya dan bergaya.",
        price: 400.0,
      },
    ],
  }));

  Alpine.store("cart", {
    items: [],
    total: 0,
    quantity: 0,
    add(newItem) {
      // cek item yang sama
      const cartItem = this.items.find((item) => item.id === newItem.id);

      // jika belum ada
      if (!cartItem) {
        this.items.push({ ...newItem, quantity: 1, total: newItem.price });
        this.quantity++;
        this.total += newItem.price;
      } else {
        this.items = this.items.map((item) => {
          if (item.id !== newItem.id) {
            return item;
          } else {
            item.quantity++;
            item.total = item.price * item.quantity;
            this.quantity++;
            this.total += item.price;
            return item;
          }
        });
      }
    },
    remove(id) {
      const cartItem = this.items.find((item) => item.id === id);

      if (cartItem.quantity > 1) {
        const cartItem = this.items.find((item) => {
          if (item.id != id) {
            return item;
          } else {
            item.quantity--;
            item.total = item.price * item.quantity;
            this.quantity--;
            this.total -= item.price;
            return item;
          }
        });
      } else if (cartItem.quantity === 1) {
        this.items = this.items.filter((item) => item.id !== id);
        this.quantity--;
        this.total -= cartItem.price;
      }
    },
  });
});

//konversi EUR
const rupiah = (number) => {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  }).format(number);
};

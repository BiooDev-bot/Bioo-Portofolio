// toggle class active
const navbarNav = document.querySelector(".navbar-nav");
// hamburger menu active
document.querySelector("#hamburger-menu").onclick = function () {
  navbarNav.classList.toggle("active");
};

//profile form onclick
document
  .querySelector(".profile-link")
  .addEventListener("click", function (event) {
    event.preventDefault(); // Mencegah link default
    const dropdownMenu = this.nextElementSibling;
    dropdownMenu.classList.toggle("show"); // Toggle class 'show'

    // Mengubah arah panah saat diklik
    const arrow = this.querySelector(".arrow-down");
    arrow.style.transform = dropdownMenu.classList.contains("show")
      ? "rotate(225deg)"
      : "rotate(45deg)";
  });

// Menutup dropdown jika user mengklik di luar dropdown
window.addEventListener("click", function (event) {
  if (!event.target.closest(".profile-dropdown")) {
    const dropdownMenu = document.querySelector(".dropdown-menu");
    if (dropdownMenu.classList.contains("show")) {
      dropdownMenu.classList.remove("show");
      document.querySelector(".arrow-down").style.transform = "rotate(45deg)";
    }
  }
});

//toggle class active shopping cart
const shoppingCart = document.querySelector(".shopping-cart");
document.querySelector("#shopping-cart-button").onclick = (e) => {
  shoppingCart.classList.toggle("active");
  e.preventDefault();
};

//klik area luar hamburger menu
const hamburger = document.querySelector("#hamburger-menu");
const sc = document.querySelector("#shopping-cart-button");

document.addEventListener("click", function (e) {
  if (!hamburger.contains(e.target) && !navbarNav.contains(e.target)) {
    navbarNav.classList.remove("active");
  }
  if (!sc.contains(e.target) && !shoppingCart.contains(e.target)) {
    shoppingCart.classList.remove("active");
  }
});

//hero section img

let currentIndex = 0;
const images = document.querySelectorAll(".hero .image-container img");
const totalImages = images.length;

function showNextImage() {
  images[currentIndex].classList.remove("active");
  images[currentIndex].classList.add("unactive");

  currentIndex = (currentIndex + 1) % totalImages;

  images[currentIndex].classList.remove("unactive");
  images[currentIndex].classList.add("inactive");

  currentIndex = (currentIndex + 1) % totalImages;

  images[currentIndex].classList.remove("inactive");
  images[currentIndex].classList.add("active");
}

// Tampilkan gambar pertama
images[currentIndex].classList.add("active");

// Ganti gambar setiap 3 detik
setInterval(showNextImage, 3000);

//about h2 transition
document.addEventListener("DOMContentLoaded", function () {
  const aboutSection = document.querySelector(".about h2");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        } else {
          entry.target.classList.remove("visible");
        }
      });
    },
    {
      threshold: 0.1, // Menyesuaikan ambang batas visibilitas
    }
  );

  observer.observe(aboutSection);
});

//transition video active
document.addEventListener("DOMContentLoaded", function () {
  const videoContainer = document.querySelector(".video-container");

  function handleScroll() {
    const rect = videoContainer.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom >= 0) {
      videoContainer.classList.add("visible");
    } else {
      videoContainer.classList.remove("visible");
    }
  }

  window.addEventListener("scroll", handleScroll);
  handleScroll(); // Check initial position
});

//transition container platforms active
document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".container");
  const stats = document.querySelector(".stats");

  function handleScroll() {
    const containerRect = container.getBoundingClientRect();
    const statsRect = stats.getBoundingClientRect();

    if (containerRect.top < window.innerHeight && containerRect.bottom >= 0) {
      container.classList.add("visible");
    } else {
      container.classList.remove("visible");
    }

    if (statsRect.top < window.innerHeight && statsRect.bottom >= 0) {
      stats.classList.add("visible");
    } else {
      stats.classList.remove("visible");
    }
  }

  window.addEventListener("scroll", handleScroll);
  handleScroll(); // Check initial position
});

//scroll bar genre section

function scrollLeft() {
  const container = document.querySelector(".horizontal-scroll");
  container.scrollBy({
    left: -container.clientWidth * 0.8,
    behavior: "smooth",
  });
}

function scrollRight() {
  const container = document.querySelector(".horizontal-scroll");
  container.scrollBy({
    left: container.clientWidth * 0.8,
    behavior: "smooth",
  });
}

// scroll btn genre section

let scrollInterval;

const scrollContainer = document.querySelector(".horizontal-scroll");
const scrollAmount = 60; // Adjust this value to control the scroll speed

const startScroll = (direction) => {
  scrollInterval = setInterval(() => {
    scrollContainer.scrollBy({
      left: direction === "right" ? scrollAmount : -scrollAmount,
    });
  }, 80); // Adjust this interval to control the scroll speed
};

const stopScroll = () => {
  clearInterval(scrollInterval);
};

document
  .querySelector(".slide-btn.left")
  .addEventListener("mousedown", () => startScroll("left"));
document
  .querySelector(".slide-btn.right")
  .addEventListener("mousedown", () => startScroll("right"));

document
  .querySelector(".slide-btn.left")
  .addEventListener("mouseup", stopScroll);
document
  .querySelector(".slide-btn.right")
  .addEventListener("mouseup", stopScroll);

document
  .querySelector(".slide-btn.left")
  .addEventListener("mouseleave", stopScroll);
document
  .querySelector(".slide-btn.right")
  .addEventListener("mouseleave", stopScroll);

// infinite scroll news section //

const pool = document.querySelector(".pool").cloneNode(true);

document.querySelector(".articles-container").appendChild(pool);

// modal box

const itemDetailModal = document.querySelector("#item-detail-modal");
const itemDetailPunker = document.querySelector("#item-detail-punker");
const itemDetailWitch = document.querySelector("#item-detail-witch");
const itemDetailValo = document.querySelector("#item-detail-valo");
const itemDetailHad = document.querySelector("#item-detail-had");
const itemDetailCyberpunk = document.querySelector(".item-detail-cyberpunk");
const itemDetailThewitcher = document.querySelector(".item-detail-thewitcher");
const itemDetailValorant = document.querySelector(".item-detail-valorant");
const itemDetailHades = document.querySelector(".item-detail-hades");
const itemDetailButton = document.querySelector(".item-detail-GOT");

itemDetailCyberpunk.onclick = (e) => {
  itemDetailPunker.style.display = "flex";
  e.preventDefault();
};

itemDetailThewitcher.onclick = (e) => {
  itemDetailWitch.style.display = "flex";
  e.preventDefault();
};

itemDetailValorant.onclick = (e) => {
  itemDetailValo.style.display = "flex";
  e.preventDefault();
};

itemDetailButton.onclick = (e) => {
  itemDetailModal.style.display = "flex";
  e.preventDefault();
};

itemDetailHades.onclick = (e) => {
  itemDetailHad.style.display = "flex";
  e.preventDefault();
};

//klik tombol close
document.querySelector(".modal1 .close1").onclick = (e) => {
  itemDetailPunker.style.display = "none";
  e.preventDefault();
};

document.querySelector(".modal2 .close2").onclick = (e) => {
  itemDetailWitch.style.display = "none";
  e.preventDefault();
};

document.querySelector(".modal3 .close3").onclick = (e) => {
  itemDetailValo.style.display = "none";
  e.preventDefault();
};

document.querySelector(".modal .close").onclick = (e) => {
  itemDetailModal.style.display = "none";
  e.preventDefault();
};

document.querySelector(".modal4 .close4").onclick = (e) => {
  itemDetailHad.style.display = "none";
  e.preventDefault();
};

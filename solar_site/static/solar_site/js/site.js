const header = document.querySelector("[data-site-header]");
const navToggle = document.querySelector("[data-nav-toggle]");
const navMenu = document.querySelector("[data-nav-menu]");
const toast = document.querySelector("[data-toast]");

if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
        navMenu.classList.toggle("is-open");
    });
}

if (header) {
    const setHeaderState = () => {
        header.classList.toggle("is-scrolled", window.scrollY > 12);
    };
    setHeaderState();
    window.addEventListener("scroll", setHeaderState, { passive: true });
}

const revealItems = document.querySelectorAll("[data-reveal]");
if (revealItems.length) {
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.18 }
    );
    revealItems.forEach((item) => observer.observe(item));
}

const showToast = (message, isError = false) => {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.toggle("is-error", isError);
    toast.classList.add("is-visible");
    window.clearTimeout(showToast.timeoutId);
    showToast.timeoutId = window.setTimeout(() => {
        toast.classList.remove("is-visible");
    }, 3600);
};

document.querySelectorAll("[data-api-form]").forEach((form) => {
    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const endpoint = form.dataset.apiEndpoint;
        const submitButton = form.querySelector('button[type="submit"]');
        const formData = new FormData(form);
        const payload = Object.fromEntries(formData.entries());

        if (submitButton) {
            submitButton.disabled = true;
            submitButton.dataset.originalText = submitButton.textContent;
            submitButton.textContent = "Submitting...";
        }

        try {
            const response = await fetch(endpoint, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            });

            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.detail || "Something went wrong.");
            }

            form.reset();
            showToast(data.message || "Submitted successfully.");
        } catch (error) {
            showToast(error.message || "Unable to submit right now.", true);
        } finally {
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.textContent = submitButton.dataset.originalText || "Submit";
            }
        }
    });
});

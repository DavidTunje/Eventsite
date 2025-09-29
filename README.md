# 🎟️ Event Management Website (Django + Tailwind)

A simple **event management web app** built with **Django** and styled using **Tailwind CSS**.  
Users can view upcoming events, see event details, and register.  
The project also exposes **JSON APIs** to fetch events and register programmatically.

---

## 🚀 Features
- 🏠 **Homepage** — lists all upcoming events in a clean card layout.
- 📄 **Event detail page** — shows full event info and a registration form.
- ✍️ **Event registration** — users can register with name + email.
- 🔗 **API endpoints** — fetch events and register via JSON (good for AJAX or external apps).
- 🛠️ **Admin panel** — manage events and registrations easily.

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** Django Templates + Tailwind CSS (via CDN)
- **Database:** SQLite (default, but can be swapped with PostgreSQL/MySQL)
- **API:** Django views returning JSON

---

## 📂 Project Structure
eventsite/ # Main Django project
events/ # Events app (models, views, templates, urls)
├── models.py # Event & Registration models
├── views.py # Homepage, detail, API endpoints
├── urls.py # Routes for web + API
├── templates/
├── events/
├── base.html
├── home.html
├── event_detail.html

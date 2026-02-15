# Inventory Alert System

A smart, web-based inventory tracking system built with Python (Flask) and SQLite. It features a premium, responsive UI with real-time stock alerts.

## Features

-   **Dashboard Overview**: View all products, quantities, and status at a glance.
-   **Smart Alerts**: Automatic visual indicators for low stock items.
-   **Inventory Management**: Easily add, delete, and update product stock levels.
-   **Premium UI**: Modern Glassmorphism design with dark mode and smooth animations.
-   **Responsive**: Works seamlessly on desktop and mobile devices.

## Tech Stack

-   **Backend**: Python (Flask)
-   **Database**: SQLite (Embedded)
-   **Frontend**: HTML5, CSS3 (Custom Glassmorphism Design)

## Prerequisites

-   Python 3.x installed on your system.

## Installation

1.  **Clone the repository** (or extract the project files):
    ```bash
    git clone https://github.com/Antoh254/Inventory-Tracker.git
    cd inventory-system
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Access the dashboard**:
    Open your web browser and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```
inventory-system/
├── app.py              # Main Flask application
├── inventory.db        # SQLite database (auto-created)
├── requirements.txt    # Project dependencies
├── static/
│   └── css/
│       └── style.css   # Custom styles
└── templates/
    └── index.html      # Main dashboard template
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

# Excel GPT Demo

This project demonstrates the integration of GPT with Excel. It provides a basis for exploring functionalities of semantic kernels and LLM-based apps. Follow the instructions below to install the requirements for both the backend and frontend, and to run the application.

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- npm (Node Package Manager)

## Backend Installation

1. Navigate to the backend directory:
    ```sh
    cd backend
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Frontend Installation

1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```

2. Install the required npm packages:
    ```sh
    npm install
    ```

## Running the Application

### Backend

1. Ensure the virtual environment is activated.
2. Start the backend server:
    ```sh
    python app.py
    ```

### Frontend

1. Navigate to the frontend directory if not already there:
    ```sh
    cd frontend
    ```

2. Start the frontend development server:
    ```sh
    npm start
    ```

The application should now be running, with the backend server typically accessible at `http://localhost:8000` and the frontend server at `http://localhost:5173` (default ports for fastapi and SvelteKit).

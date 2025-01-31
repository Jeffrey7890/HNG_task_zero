# Backend API for HNG12 Stage 0

## Project Description
This repository contains the code for the public API that returns basic information about the developer, including:
- Registered email address
- Current date and time (ISO 8601 format)
- GitHub URL of the project's codebase

The API is built using **Python**, **Flask**, and **Flask-CORS** for handling CORS requests, and deployed with **Gunicorn**.

## API Endpoint

### **GET** `/`

#### **Response Example (200 OK):**
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Jeffrey7890/HNG_task_zero.git"
}
```

#### **Fields:**
- **email**: The registered email address.
- **current_datetime**: The current date and time in ISO 8601 format (UTC).
- **github_url**: A link to the repository's GitHub page.

## Technology Stack
- **Programming Language**: Python
- **Framework**: Flask
- **CORS Handling**: Flask-CORS
- **Deployment**: Gunicorn (for production deployment)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Jeffrey7890/HNG_task_zero.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API locally using Flask:
   ```bash
   python app.py
   ```
   This will start the API locally on `http://localhost:5000`.

4. To run the API in production, use Gunicorn:
   ```bash
   gunicorn app:app
   ```

## Deployment

This API is deployed at https://hng-task-zero-vizn.onrender.com

## CORS Handling
The API is configured to handle Cross-Origin Resource Sharing (CORS) requests from different origins using **Flask-CORS**.

## Testing the API
To test the API, you can send a GET request to the endpoint:

```bash
curl http://https://hng-task-zero-vizn.onrender.com/
```

You should receive a JSON response similar to the one shown above.

## Backlink
For more details on Python development, visit:  
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### `requirements.txt`

Make sure your `requirements.txt` file includes the necessary dependencies:
```
Flask
Flask-CORS
gunicorn
```

# Email Campaign Manager API

# Project Setup

### . Create a project folder name main
## create virtualenv  and activate
> python -m venv venv
> venv\bin\activate

### . Install requirements
> pip install -r requirements.txt

### . Run migrations

> python manage.py makemigrations

> python manage.py migrate

###. Run the project

> python manage.py runserver
> 
# Celery Setup

### 1. Open new terminal

### 2. Activate the enviroment
> venv\Scripts\activate
> 
### 3. Run below command
> celery -A email_campaign worker -l INFO
> celery -A email_campaign beat -l INFO

The Email Campaign Manager API is a Django-based RESTful API that allows you to manage subscribers, campaigns, and send daily email campaigns using SMTP or an external service like Mailgun.

## Endpoints

### Subscribers

- **Add Subscriber**
  - **Endpoint**: `/api/subscribers/`
  - **Method**: POST
  - **Description**: Add a new subscriber to the system.
  - **Request Body**:
    ```json
    {
        "email": "yourmail@com",
        "first_name": "test"
    }
    ```
  - **Response**:
    - HTTP Status: 201 Created

- **Unsubscribe Subscriber**
  - **Endpoint**: `/api/subscribers/{subscriber_id}/unsubscribe/`
  - **Method**: PUT
  - **Description**: Unsubscribe a user by marking them as inactive.
  - **Response**:
    - HTTP Status: 200 OK
    - Response Body: {"message": "user unsubscribed succesfully!"}

### Campaigns

- **Add Campaign**
  - **Endpoint**: `/api/campaigns/`
  - **Method**: POST
  - **Description**: Add a new campaign to the system.
  - **Request Body**:
    ```json
    {
        "subject": "Campaign Subject",
        "preview_text": "Preview Text",
        "article_url": "https://example.com/article",
        "html_content": "<p>...</p>",
        "plain_text_content": "Text content..",
        "published_date": "2023-09-08"
    }
    ```
  - **Response**:
    - HTTP Status: 201 Created

## Usage

To use this API, you can make HTTP requests to the specified endpoints using tools such as Insomnia, Postman, or Python's requests library.

## Additional Features

- Used Django Rest Framework for building RESTful endpoints.
- Created a custom management command for creating email campaigns.
- Intergarted an external email service Mailgun for sending campaigns daily.
- Used Celery and Celery Beat for asynchronous email campaign scheduling. 
- Used Redis as a message broker for Celery.
- 


